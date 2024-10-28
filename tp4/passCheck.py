import re


def passCheck(nom):
    regexp=  r'[0-9]{2}'
    regexp2= r'[\w]{8,12}'
    regexp3= r'[a-z]{1}'
    regexp4 = r'[A-Z]{1}'

    automate=re.compile(regexp)
    automate2 = re.compile(regexp2)
    automate3=re.compile(regexp3)
    automate4 = re.compile(regexp4)

    ok=automate.findall(nom)
    ok2=automate2.findall(nom)
    ok3=automate3.findall(nom)
    ok4 = automate4.findall(nom)


    if(ok!=[] and ok2!=[] and ok3!=[] and ok4!=[]):
        print("valide")
    else:
        print("erreur")

print()

password=input("saisir un mot de passe")

passCheck(password)
