def is_pytagoricien(x,y,z):
    if((x<y) & (y<z) & ((x**2)+(y**2)==(z**2))):
        return True
    else:
        return False

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if(is_pytagoricien(x,y,z)):
                print(x,y,z)
