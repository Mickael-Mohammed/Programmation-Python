import re
import numpy as np
import matplotlib.pyplot as plt

def connexions(file):

    #ouverture du fichier
    f=open(file,"r")

    #lecture du fichier
    text=f.readlines()

    #L'expression regulière de la date est caractérisé par 2 chiffres ,suivi de 3 lettres et enfin de 4 chiffres ,
    # chaque ensemble étant séparée par des /

    regexp="[0-9]{2}/[a-zA-Z]{3}/[0-9]{4}"

    automate=re.compile(regexp)
    regexp2 = r'[a-zA-Z]{3}/[0-9]{4}'
    automate2 = re.compile(regexp2)
    regexp3 = r'[0-9]{4}'
    automate3 = re.compile(regexp3)


    # liste contient les dates du fichier
    liste=[]
    liste2=[]
    liste3=[]
    for line in text:

        ok=automate.findall(line)

        liste.append(ok)
        ok2=automate2.findall(line)
        ok3=automate3.search(line)
        liste2.append(ok2)
        liste3.append(ok3)

    #Tous les mois de toutes les annees
    moisAnnees=[]
    annee=[]
    for ok2 in liste2:
        moisAnnees.append(ok2[0])
    for ok3 in liste3:
        annee.append((ok3[0]))




    reg=input("afficher le nombre de connexions par mois/Année, entrez l'année :")


    automateReg=re.compile(reg)

    #chercher tous les mois d'une année (mois/annee peut etre répétitif)
    #dates est une liste qui contient des objets de type mois/annee avec annee une unique année
    dates=[]
    for m in moisAnnees:
        ok4=automateReg.search(m)
        if(ok4!=None):
            dates.append(m)


    #Contient des objets de meme type que date mais une unique fois
    dateUniques=[]
    for date in dates:
        if(dateUniques.__contains__(date)==False):
            dateUniques.append(date)
    print(dateUniques)

    regexpMois="[a-zA-Z]{3}"
    automate5=re.compile(regexpMois)

    #les mois de l'année XXXX
    moisAnneeX=[]
    for m in dates:
        ok5=automate5.findall(m)
        moisAnneeX.append(ok5)


    #liste de mois uniques
    moisUniques=[]

    #liste : mois d'une année, nombre de connexions pour chaque mois d'une année

    moisUniquesCount=[]
    for m in moisAnneeX:
        if(moisUniques.__contains__(m)==False):
             moisUniques.append(m)
             objet=[]
             objet.append(m)
             count=1
             objet.append(count)
             moisUniquesCount.append(objet)
        else:
            for objet in moisUniquesCount:
                if(objet[0]==m):
                    objet[1]=objet[1]+1

    #print(moisUniquesCount)

    #ABSCISSE DU GRAPHE (mois/annee)
    xlabels=[]

    #ORDONNE DU GRAPHE  (nombre de connexions)
    ylabels=[]

    for date in dateUniques:
        xlabels.append(date)

    for object in moisUniquesCount:

        ylabels.append(object[1])
    print(xlabels)
    print(ylabels)
    x=np.array(xlabels)
    y=np.array(ylabels)
    plt.plot(x,y)
    plt.show()


file=input("saisir le chemin du fichier")
connexions(file)