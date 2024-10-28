def perfect(x):
    somme=0
    for y in range(1,x):
        if(x%y==0):
            somme+=y
    if(x==somme):
        return True
    else:
        return False


for x in range (1,999):
    if(perfect(x)==True):
        print(x)