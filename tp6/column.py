import self as self


import pawn


class Column():

    tableau=[]
    hauteur=0

    def __init__(self, hauteur,toPrint=None):

        tab = []
        for h in range(0, hauteur):
            l = []
            # on a une seule colonne constitué de 4 caractéres , un + et 3 -

            for i in range(0, (4)):

                if (i % 4 == 0):
                    l.append("+")
                else:
                    l.append("-")
            l.append("+")

            # ce processus ne prend pas en compte la dernière ligne du tableau
            # nous allons donc la stocker dans une variable et l'afficher à la fin

            derniereLigne = l
            if(toPrint==None):
                print(''.join(l))

            tab.append(''.join(l))

            # création des lignes contenant | suivi de 3 espaces
            # chaque ligne de ce type est stocké dans la liste m

            m = []
            for i in range(0, (4)):
                if (i % 4 == 0):
                    m.append("|")
                else:

                    m.append(' ')

            m.append("|")

            if (toPrint == None):
                print(''.join(m))
            tab.append(''.join(m))

        if (toPrint == None):
            print(''.join(derniereLigne))
        tab.append(''.join(derniereLigne))


        self.tableau1=tab
        self.h=hauteur
        tableau=tab

    classmethod
    def drop(self,X):


        tab=self.tableau1

        print(" Affichage de la nouvelle colonne :")
        symbole=str(X)
        # liste d'indices du tableau contenant chacune des lignes de la colonne
        # on va parcourir uniquement les éléments impair du tableau car ce ce sont qui contiennent ou non des cases vides

        indices=[]
        for x in range(0,(2*(self.h))+1):
            if(x%2==1):
                indices.append(x)

        # liste de numérotation des pions

        #une colonne est une liste de lignes
        # on va parcourir la colonne en ordre inverse pour savoir qu'elle est la dernière case déjà remplie
        rev=reversed(indices)

        # Pour chaque ligne de la colonne
        for x in rev:

            line=tab[x]
            if (x == 1):
                if (line[2]!=' '):
                    print("tableau remplie")
                    break
                # On vérifie si la ligne courante contient déjà un pion ou non
            if(line[2]==' '):

                    # si la ligne ne contient pas de pion on peut ajouter le pion à la case vide

                self.tableau1[x]="| "+symbole+" |"

                    # On passe au pion suivant à déposer
                break

            # affichage du tableau contenant les pions

        for line in self.tableau1:
            print(line)











