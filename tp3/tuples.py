


def minmax( liste ):

    min=liste[0]
    max=liste[0]
    for x in liste:
        if(x<min):
            min=x
        if(x>max):
            max=x

    liste2=[]
    liste2.append(min)
    liste2.append(max)
    print(liste2)
    moyenne = (liste2[0] + liste2[1]) / 2
    print("La moyenne est ",moyenne)

liste=[9, 7, 3, 2, 7, 8, 3, 8, 4, 2, 7, 0, 5, 3, 2, 0, 9, 6, 0, 5, 6, 2, 2, 4, 5, 2, 6, 3, 5, 2]
liste2=minmax(liste)

