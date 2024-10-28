import random
import statistics

liste=[]
for y in range(1,20):
    x=random.random()
    liste.append(x)

print(liste)

somme=0
n=20

for x in liste:
    somme+=x

print("La moyenne est ",somme/n)

moyenne=somme/n

liste.sort()
listePetit=[]
listeGrand=[]
for x in liste:
    if(x<=moyenne):
        listePetit.append(x)
    else:
        listeGrand.append(x)

print("La liste des valeurs plus petit ou égale à la moyenne :")
print(listePetit)

print("La liste des valeurs plus grand que la moyenne :")
print(listeGrand)

print("La médiane est",liste[9])
mediane=liste[9]

medianeInf=[]
medianeSup=[]


for x in liste:
    if(x<=mediane):
        medianeInf.append(x)
    else:
        medianeSup.append(x)

print("La liste des valeurs plus petit ou égale à la médiane :")
print(medianeInf)
print("La liste des valeurs plus grand que la médiane :")
print(medianeSup)
