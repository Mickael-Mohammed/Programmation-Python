import re

def noHtml(nom):

    f = open(nom, "r")

    text=f.readlines()
    print(text)
    automate = re.compile('<.*?>')
    texte2=[]
    for line in text:

        ok=automate.findall(line)
        print(ok)
        for balise in ok:
            newLine=re.sub(balise,"",line)
            line=newLine
        print(line)
        texte2.append(line)

    print(texte2)
    f2=open(nom,"w")

    f2.write("")

    f2=open(nom,"a")
    for line in texte2:
        f2.write(line)

    #Création d'un fichier avec l'extension .nohtml
    print(nom)
    regexp2="\.html"
    automate2=re.compile(regexp2)
    ok2=automate2.search(nom)
    print(ok2)
    newName=re.sub(regexp2,".nohtml",nom)
    print(newName)

    newFile=open(newName,"a")
    for line in texte2:
        newFile.write(line)

    print("création d'un nouveau fichier avec l'extension .nohtml avec succès!")


name=input("indiquez le chemin du fichier html à transformer")
noHtml(name)

