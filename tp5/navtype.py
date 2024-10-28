import re
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2


def navtype(file):

    f=open(file,"r")
    text=f.readlines()

    regexp='Mozilla|Chrome|Opera|Safari' ;
    regexp2="Windows|Linux|Mac OS"

    automate=re.compile(regexp)
    automate2=re.compile(regexp2)

    #liste contenant des listes de navigateurs pour toutes les connexions
    navigateur=[]

    #liste contenant tous les systèmes pour toutes les connexions
    systeme=[]
    for line in text:

        ok=automate.findall(line)
        ok2=automate2.findall(line)

        if(ok!=None):
            navigateur.append(ok)

        if(ok2!=None):
            systeme.append(ok2)

    connexionsOpera=0
    connexionsChrome=0
    connexionsMozilla=0
    connexionsSafari=0
    connexionsWindows=0
    connexionsLinux=0
    connexionMacOS=0

    #Dans un OS on peut utiliser plusieurs navigateurs
    #calcul du nombre de connexions pour un navigateur spécifique
    for n in navigateur:

        if(n.__len__()!=0):
            for m in n:
                if(m=="Opera" ):
                    connexionsOpera+=1
                if(m=="Chrome" ):
                    connexionsChrome+=1
                if(m=="Mozilla"):
                    connexionsMozilla+=1
                if(m=="Safari"):
                    connexionsSafari+=1



    #calcul du nombre de connexions pour un OS spécifique
    for s in systeme:
        if(s.__len__()!=0):
            if(s[0]=="Windows"):
                connexionsWindows+=1
            if(s[0]=="Linux"):
                connexionsLinux+=1
            if(s[0]=="Mac OS"):
                connexionMacOS+=1

    print("")
    print("Connexions par navigateur :")
    print("Nombre de connexions sur Opera",connexionsOpera)
    print("Nombre de connexions sur Chrome",connexionsChrome)
    print("Nombre de connexions sur Mozilla",connexionsMozilla)
    print("Nombre de connexions sur Safari",connexionsSafari)

    print("")
    print("Connexions par système d'exploitation :")
    print("Nombre de connexions sur Windows",connexionsWindows)
    print("Nombre de connexions sur Linux",connexionsLinux)
    print("Nombre de connexions sur Mac OS",connexionMacOS)

    print("")
    print("nb: pour obtenir du graphe des connexions par systèmes d'exploitation , fermer la fenetre du graphe de connexions par navigateur")
    couleurs = ['blue', 'orange', 'green','yellow']
    legende = 'Opera', 'Chrome', 'Mozilla','Safari'
    taille = [connexionsOpera, connexionsChrome, connexionsMozilla,connexionsSafari]

    #création et affichage des graphes
    plt.pie(taille, labels=legende, colors=couleurs,
            autopct='%1.1f%%', startangle=90)

    plt.axis('equal')
    plt.savefig("connexions par navigateur.png")
    plt.show()

    couleurs2=['blue', 'orange', 'green']
    legende2='Windows','Linux','MacOS'
    taille2=[connexionsWindows,connexionsLinux,connexionsSafari]

    plt2.pie(taille2, labels=legende2, colors=couleurs2,
            autopct='%1.1f%%', startangle=90)

    plt2.axis('equal')
    plt2.savefig("connexions par système.png")
    plt2.show()


file=input("saisir le chemin du fichier")
navtype(file)