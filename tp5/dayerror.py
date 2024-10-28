import re

def dayerror(nom):

    #ouverture du fichier en mode lecture
    f=open(nom,"r")

    #la liste text est une liste contenant chacune des lignes du fichier
    #Donc un élement de cette liste est une ligne du fichier
    text=f.readlines()

    # La date est normalisé ici par 3 lettres pour le jour, suivi de 3 lettres pour le moid et enfin de 2 chiffres pour le jour, d'ou l'expression regulière ci-dessous
    regexp="[a-zA-Z]+\s+[a-zA-Z]+\s+[0-9]+"
    automate=re.compile(regexp)

    #Dates est une liste de dates
    Dates=[]

    #size indique la taille de la liste Dates
    size=0
    for line in text:
        size=size+1
        ok=automate.findall(line)
        Dates.append(ok)


    i=0
    count=0

    #l est une liste de compteurs qui contient pour chaque date, le nombre de fois qu'elle apparait dans une liste
    l=[]
    for date in Dates:
        #on compte pour une date de donnée le nombre de fois qu'elle apparait dans la liste de Dates
        count=Dates.count(date)


        if(l.__contains__(count)==False):
            l.append(count)

    #la liste dates uniques contient toutes les dates une seule fois
    datesUniques=[]

    #size 2 est la taille de la liste de dates uniques
    size2=0

    for date in Dates:
        if(datesUniques.__contains__(date)==False):
            size2+=1
            datesUniques.append(date)

    #affichage d'une date unique suivi de son nombre d'erreurs
    for i in range(0,size2):
            print(datesUniques[i],"  ",l[i])


    #calcul du nombre total d'erreurs
    sum=0
    for count in l:
        sum=sum+count


    #calcul de la moyenne d'erreurs par jour
    moyenne=sum/size2
    print("\n")
    print("La moyenne du nombre d'erreurs par jour est : ",moyenne)


file=input("saisir le chemin du fichier :")
dayerror(file)