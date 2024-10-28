import column

class Pawn():

    def __init__(self,arg):

        if(arg!="X" and arg!="O"):
            print("erreur: les seuls pions autorisés sont X ou O")
            return None
        else:
            self.arg=arg

    def __repr__(self):
        # affichage d'un pion

        return f"{self.arg}";



