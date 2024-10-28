import re


def urlerror(file):

    #ouverture du fichier en mode lecture
    f=open(file, "r")

    #chaque ligne du fichier est lue et placé dans la liste text. text est une liste dont chaque élément est une ligne du fichier.
    text=f.readlines()

    #toutes les url dans le fichier commencent par  "/var/www/www.almhuette-raith.at/"  suivie du reste de l'url
    #l'url est le dernier élement d'une ligne, d'ou l'expression regulière ci-dessous

    regexp=r"/var/www/www.almhuette-raith.at/.*$"
    automate=re.compile(regexp)

    #l est une liste qui pour chaque ligne du fichier continent l'expression regulière recherché
    # l est donc une liste contenant toutes les url du fichier
    l=[]

    for line in text:
        ok2=automate.findall(line)
        l.append(ok2)

    # unique2 est une liste contenant chacune des url du fichier une et une seule fois
    unique2=[]

    # erreursUrl est une liste spéciale qui contiendra 2 éléments
    # erreursUrl contiendra une url et le nombre d'élements associé à cette url
    # Donc pour un ensemble d'url donné on aura un ensemble de liste erreurs contenant à chaque fois une url et le nombre d'erreurs associé à cette url
    # enfin pour chaque liste erreursUrl on l'ajoute à la liste erreurs au moment de la création de erreursUrl

    #la liste erreurs et donc la liste qui contient des objets de type une url suivie de son nombre d'erreurs
    erreurs=[]

    for ok2 in l:

        if(unique2.__contains__(ok2)==False):
            unique2.append(ok2)

            nbErreur=1

            #création de la liste erreur
            erreurUrl=[ok2,nbErreur]


            erreurs.append(erreurUrl)

        else:
            for erreurUrl in erreurs:
                if(erreurUrl[0]==ok2):
                    erreurUrl[1]=erreurUrl[1]+1

    #somme sert à calucler la somme totale des erreurs d'url
    somme = 0

    #affichage itératif de chacune des url suivie de son nombre d'erreurs asscoié
    for erreurUrl in erreurs:
        print(erreurUrl[0]); print(erreurUrl[1])
        somme+=erreurUrl[1]


    print(somme," erreurs en défaut")


file=input("saisir le chemin du fichier")
urlerror(file)