import re
import matplotlib.pyplot as plt

def ipclasses(file):


    f=open(file,"r")
    text=f.readlines()

    #une adresse ip se retrouve ici en début de chaque ligne du fichier access.log
    #une adresse ip est divisée en 4 numéros et chacun de ces numéros varie de 0 à 255
    #un numéro est constitué de 1 à 3 chiffres et chaque chiffre varie de 0 à 9
    #l'expression regulière ci-dessous nous permet de récupérer une adresse ip
    regex=r"^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}"


    #l'expression regulière ci-dessous nous permet de recupérer le 1er champ de l'adresse ip qui définit sa classe
    regex2="^[0-9]{1,3}"

    automate=re.compile(regex)
    automate2=re.compile(regex2)

    #liste est une liste d'élements qui contient pour chaque ligne du text , le premier numéro de l'adresse ip associé qui indique sa classe
    liste=[]
    for line in text:
        ok=automate.findall(line)
        ok2=automate2.findall(line)

        conversion=int(ok2[0])
        liste.append(conversion)



    #nombre d'adresse ip de la classe A
    nbA=0

    #nombre d'adresse ip de la classe B
    nbB=0

    #nombre d'adresse ip de la classe C
    nbC=0

    #nombre d'adresse ip des autres classes
    autres=0


    for n in liste:
        if(n>=0 and n<=126):
            #une adresse ip est de la classe ip si son premier numéro est compris entre 0 et 126
            nbA+=1
        if(n>=128 and n<=191):
            #adresse ip de classe B
            nbB+=1
        if(n>=192 and n<=223):
            #adresse ip de classe C
            nbC++1
        if(n>=224 and n<=239):
            #adresse ip de classe D
            autres+=1
        if(n==127):
            #adresse de boucle locale
            autres+=1
        if(n>=240 and n<=255):
            #adresse de classe E ou classe Multicast
            autres+=1

    #affichage des résultats
    print("classe A ",nbA)
    print("classe B ", nbB)
    print("classe C ", nbC)
    print("autres   ",autres)

    #labels des classes
    legende='classe A', 'classe B','classe C', 'autres'
    taille=[nbA,nbB,nbC,autres]

    #couleurs pour chaque classe ip dans le camembert
    couleurs = ['blue', 'orange', 'green', 'red']

    #création du graphe
    plt.pie(taille, labels=legende, colors=couleurs,
            autopct='%1.1f%%', startangle=90)

    plt.axis('equal')

    #sauvegarde de notre graphe dans un fichier image
    plt.savefig('exo4.png')

    #affichage du graphe
    plt.show()


file=input("saisir le chemin du fichier")
ipclasses(file)


