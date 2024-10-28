def copy(file1,file2):

    try:
        f1=open(file1,"r")
    except IOError:
        print("cannot open")
    except FileNotFoundError:
        print("error cannot open")

    try:
        f2=open(file2,"w")
    except FileNotFoundError:
        print("cannot open")


    f2.write(f1.read())

copy("C:\\Users\micka\OneDrive\Bureau\\lisa.txt","C:\\Users\micka\OneDrive\Bureau\\amelie.txt")