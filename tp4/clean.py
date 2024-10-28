import re


def clean(nom):
    f = open(nom, "r")
    l = []
    text = f.readlines()
    # print(text)
    regex = r"\s\s+"
    regexp2 = "^\s+"
    regexp3 = "\t+"
    regexp4 = "\s+$"
    automate = re.compile(regex)  # automate pour supprimer les espaces en trop
    automate2 = re.compile(regexp2)  # supprimer les espaces de début
    automate3 = re.compile(regexp3)  # supprimer les tabultations
    automate4 = re.compile(regexp4)  # supprimer les espaces de fin (invisibles)

    regexp5 = r"\s[:;,.]"
    regexp6 = '\?+'
    automate5 = re.compile(regexp5)
    automate6 = re.compile(regexp6)

    cleanText = []
    for line in text:

        ok = automate.findall(line)
        ok2 = automate2.findall(line)
        ok3 = automate3.findall(line)
        ok4 = automate4.findall(line)
        ok5 = automate5.findall(line)
        ok6 = automate6.findall(line)
        newLine = line
        if (ok != []):
            for moreSpace in ok:
                newLine = re.sub(regex, " ", line)
                line = newLine

        newLine2 = newLine
        if (ok2 != []):
            for startWithSpace in ok2:
                newLine2 = re.sub(regexp2, "", line)

                # on remplace les espaces de début de ligne par aucun espace en début de ligne

            # on se sert de la ligne supprimé des espaces en trop et des début d'espaces pour créer une ligne supprimé des tabultations

        newLine3 = newLine2
        if (ok3 != []):
            for tab in ok3:
                newLine3 = re.sub(regexp3, " ", newLine2)

                # on remplace les tabultations par un expace

        newLine4 = newLine3
        if (ok4 != []):
            for EndingWithSpace in ok4:
                newLine4 = re.sub(regexp4, "", newLine3)
                # on remplace les espaces de fin de texte par aucun espace en fin de texte

        newLine5 = newLine4

        if (ok5 != []):
            for wrongSpaceBefore in ok5:
                print(wrongSpaceBefore)
                char = wrongSpaceBefore[1]
                if (char != '.'):
                    newLine5 = re.sub(wrongSpaceBefore, char, newLine5)
                else:
                    re.sub(wrongSpaceBefore,".", newLine5)

        newLine6 = newLine5
        if (ok6 != []):

            for withoutSpace in ok6:
                newLine6 = re.sub(regexp6, " ?", newLine6)
        cleanText.append(newLine6)

    print(cleanText)

    newName = nom + ".clean"

    # écriture du contenu clean dans un nouveau fichier d'extension .clean
    f2 = open(newName, "w")
    for line in cleanText:
        f2.write(line)
        f2.write("\n")



a=input("Entrez le chemin du fichier")
clean(a)
