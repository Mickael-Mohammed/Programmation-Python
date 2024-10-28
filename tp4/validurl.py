import re
def valid(nom):


    regexp2="(https|http|ftp)://[A-Za-z0-9]+.[A-Za-z0.9]+(:\d)?"

    automate=re.compile(regexp2)
    ok=automate.search(nom)
    print(ok)
    if(ok==None):
        print("erreur : url invalide")
    else:
        print("url valide !")


url=input("tapez votre url !")
valid(url)