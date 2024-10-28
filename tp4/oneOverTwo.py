

def fun(nom):
    f=open(nom,"r")
    i=0
    for line in f:
        if(i%2==0):
            print(line)
        i=i+1

fun("C:\\Users\micka\OneDrive\Bureau\la fontaine.txt")

