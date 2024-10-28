import math
def sintest(x):
    if(x==0):
        return("Pas possible avec 0.0")
    else:
        return(math.sin(x)/x)


for x in range(-6,7):
    print(sintest(x/2))