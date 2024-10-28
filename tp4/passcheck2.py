
def pass2(password):
    liste=['2019','2018','abcde','0000','1234']
    if(password in liste):
        print("erreur : mot de passe interdit")
    else:
        print("mot de passe non contenue dans la liste des mots interdits")
        print("veuillez resaisir votre mot de passe")
        import  passCheck

        passCheck.passCheck(password)




mdp=input("saisir un mot de passe")
pass2(mdp)