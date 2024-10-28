liste=[9, 7, 3, 2, 7, 8, 3, 8, 4, 2, 7, 0, 5, 3, 2, 0, 9, 6, 0, 5, 6, 2, 2, 4, 5, 2, 6, 3, 5, 2]
print(liste)

impaires=[]
paires=[]
paires2=[]

for x in liste:
    if(x%2==0):
        paires.append(x)
    if((x%2==0) & (x>4)):
        paires2.append(x)
    else:
        impaires.append(x)


print(impaires)
print(paires)
print(paires2)




