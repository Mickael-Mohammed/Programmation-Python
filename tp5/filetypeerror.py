import re


def fileTypeError(file):

    #ouverture du fichier en mode lecture
    f=open(file,"r")

    text=f.readlines()

    #expression regulière de la date
    #La date est normalisé ici par 3 lettres pour le jour, suivi de 3 lettres pour le moid et enfin de 2 chiffres pour le jour
    regexp = r"[a-zA-Z]+\s+[a-zA-Z]+\s+[0-9]+"

    regexp2=  r"/var/www/www.almhuette-raith.at/.*$"

    automate=re.compile(regexp)
    automate2=re.compile(regexp2)

    #liste 1 est une liste d'url
    liste1=[]

    # liste2 est une liste d'éléments contenant chacun 2 éléments : la date et une url
    liste2=[]

    for line in text:

        # l est une liste contenant une seule date et l'url correpondant
        l=[]

        #on ajoute une date à l
        ok=automate.findall(line)
        l.append(ok)

        #on ajoute l'url correpondant à l
        ok2=automate2.findall(line)
        l.append(ok2)

        liste1.append(ok2)
        liste2.append(l)


    #unique est une liste contenant chacune des url une et une seule fois
    unique=[]

    #uniques est une liste de plusieurs listes dont chaque liste est du format=[url, date de première mise en défut, date de dernière mise en défaut]
    uniques=[]

    for l in liste2:

        if(unique.__contains__(l[1])==False):

            unique.append(l[1])

            #contient la première date de mise en défaut
            dates=[]

            dates.append(l[0])

            #m est une liste contenant à sa création l'url et sa première date de mise en défaut
            m=[]
            somme=1
            m.append(l[1])
            m.append(somme)
            m.append(dates)

            uniques.append(m)

        #Sinon on va ajouter la dernière date courante correpondant à cette url

        else:
            for m in uniques:
                if(m[0]==l[1]):
                    m[1]=m[1]+1
                    #on ajoute la dernière date de défaut de l'url à la sous-liste contenant déjà l'url et sa date de première mise en défaut
                    m.append(l[0])


    #compter les erreurs par type d'url


    final=[]
    i=0
    for m in uniques:

        #liste repectant le format d'affichage imposé par l'énoncé
        resp=[]

        #s est la longueur de la liste et nous servira à recupérer la dernière date de mise en défaut de l'url
        s=m.__len__()

        #affichage de l'url en défaut
        resp.append(m[0])

        #affichage du nombre d'erreurs associé à l'url
        resp.append(m[1])

        #affichage de la première date de mise en défaut
        resp.append(m[2])

        #nous aurons à la fin une liste de dates associé à l'url
        #Pour avoir la dernière date en défaut en recupère la dernière date de la liste
        resp.append(m[s-1])
        print(resp[0]," ",resp[1]," ",resp[2]," ",resp[3])




file=input("entrez le chemin du fichier")
fileTypeError(file)
