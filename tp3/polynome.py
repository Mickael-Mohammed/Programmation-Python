def polynome(x):
    return(3*(x**2)+5*x-10)

print(polynome(0))
for x in range(-10,11):
    print("P(%f)=%f"%(x/2,polynome(x/2)))
