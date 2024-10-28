import column
import pawn

class Grid():
    def __init__(self,hauteur,nbColonnes,symbole=None):


        self.nbColonnes1=nbColonnes
        colonnes=[]

        # Cette variable contiendra le tabelau final sous forme d'une seule chaine de caractère dans une liste
        self.tableau=[]

        # création d'un tableau contenant un ensemble de colonnes
        for col in range (0,nbColonnes):

            colonne=[]

            # création d'une colonne
            column.Column.__init__(self,hauteur,False)

            colonne=self.tableau1
            # Ajout de cette colonne à notre liste de colonnes
            colonnes.append(colonne)

        # une colonne est une liste de lignes

        tab=[]
        for colonne in colonnes:
            col1=[]
            for line in colonne:
                #on crée une liste d'une liste
                col=line
                col1.append(col)

            tab.append(col1)



        final=[]
        l=[]
        line=[]
        for x in range(0,(2*hauteur)+1):
            for t in tab:
        #Pour un numéro de ligne on va afficher cette ligne pour toutes les colonnes
                l.append(t[x])
                # ajout des sauts de lignes
            l.append('\n')


        print(final.append(''.join(l)))


        # Liste contenant un seul élément : le tableau qu'on veut afficher
        self.tableau=final



    classmethod
    def drop(self,position,symbole):
        symbole1=str (symbole)




        tab=self.tableau


        fin=False
        # une ligne dans notre tableau a 2 formes
        # +---++---++---++---+ (autant de fois que le nombre de colonnes ) suivi d'un retour à la ligne
        # |   ||   ||   ||   | (autant de fois que le nombre de colonnes ) suivi d'un retour à la ligne
        # notre tableau réalise une alternace de ces 2 types de lignes
        # notre tableau est une unique chaine de caractères

        # le numero du caractére qui pourrait contenir une case vide
        # x1 est une variable spéciale
        # Rappel: notre tableau est une chaine de caractères de la forme : +---++----+(autant de fois que le nombre de colonnes) suivi de |   ||   |(autant de fois que le nombre de colonnes) Le tout autant de fois que le nombre de lignes
        # Pour connaitre la position exacte de la 1 ère case libre il faut calculer le nombre de cases constituant la 1ère ligne plus le nombre de cases de la 2ème ligne jusqu'au numéro de colonnes indiquée

        # x1 est une valeur universel
        x1 = (5 * self.nbColonnes1) + 1 + ((position - 1) * 5) + 2

        # x sera incrementé à cahque itération de x1 et du décalage de la case pour connaitre la position de la case suivante éventuellement libre
        x=x1
        # decalage entre la dernière case de la colonne et la case ou on doit insérer le symbole
        # on calcule la longeur totale des caractères de toute une ligne (contenant un ensemble de cases)

        # le décalage entre la position de la case à vérifier et la fin de la ligne correpondant (retour à la ligne inclus)
        decalage = 5 * self.nbColonnes1 - (((position - 1) * 5) + 1)
        new1=[]
        # La variable fin permet de savoir si la case suivante contient déjà un symbole
        while(fin==False):

            #on ajoute le seul élément de tab à une varaibale tab1 pour avoir une chaine de caracteres
            tab1=tab[0]

            #calcul de la taille de la chaine
            size=len(tab1)

            if(x<size):

                #on vérifie si la case est vide donc s'il elle ne contient pas de symbole
                if(tab1[x]==' '):

                    #conversion de la chaine de caractères en une liste de caractères
                    l=[]
                    for char in tab1:
                        l.append(char)

                    # on modifie la case vide par le symbole à ajouter
                    l[x]=symbole1

                    # On regroupe à nouveau tous les caractères en une seule chaine de caractères
                    new=''.join(l)

                    #on affiche le nouveau tableau correpondant contenant le symbole

                    print(new)

                    new1=new
                    x += x1
                    #on passe à la case suivante
                    x += decalage

            else:

                fin=True
                break

        self.tableau = new1