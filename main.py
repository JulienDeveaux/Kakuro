import math
import random
import time


def main(tableauResolution=None, tableauIndice=None):
    global tailleGrille
    global wrongMask
    choice = input("Please select your grid size choice : \n6*6 : 1\n8x8 : 2\n12*12 : 3\n15x15 : 4\ntaille de grille maximale avec un résultat garanti en mois d'une minute : 12x12\n")
    starter = False
    easy = False
    exempleProf = False
    medium = False

    if choice == "1":
        starter = True
    if choice == "2":
        exempleProf = True
    if choice == "3":
        easy = True
    if choice == "4":
        medium = True

    if starter:
        tailleGrille = 6  # contrainte [bas, droite]
        tableauIndice = [
            [0, [4, 0], [9, 0], 0, 0, 0],
            [[0, 3], 0, 0, [24, 0], 0, 0],
            [[0, 17], 0, 0, 0, [17, 0], 0],
            [0, [0, 18], 0, 0, 0, 0],
            [0, 0, [0, 16], 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        tableauResolution = [
            [None, None, None, None, None, None],
            [None, 4, 5, None, None, None],
            [None, 0, 6, 0, None, None],
            [None, None, 1, 2, 3, None],
            [None, None, None, 0, 8, None],
            [None, None, None, None, None, None]
        ]
        wrongMask = [
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""]
        ]
    if easy:
        tailleGrille = 12  # contrainte [bas, droite]
        tableauIndice = [
            [0, [4, 0], [22, 0], 0, 0, [25, 0], [9, 0], 0, 0, [17, 0], [19, 0], 0,
             0],
            [[0, 8], 0, 0, [8, 0], [0, 16], 0, 0, [16, 0], [16, 10], 0, 0, [16, 0],
             0],
            [[0, 7], 0, 0, 0, [16, 39], 0, 0, 0, 0, 0, 0, 0, 0],
            [0, [15, 23], 0, 0, 0, 0, [24, 17], 0, 0, [19, 12], 0, 0,
             0],
            [[0, 7], 0, 0, [25, 6], 0, 0, 0, [9, 13], 0, 0, 0, 0, 0],
            [[0, 27], 0, 0, 0, 0, [6, 21], 0, 0, 0, 0, [36, 0], 0, 0],
            [0, [0, 16], 0, 0, [18, 9], 0, 0, 0, [23, 17], 0, 0, [6, 0],
             0],
            [0, 0, [21, 16], 0, 0, 0, 0, [21, 20], 0, 0, 0, 0,
             0],
            [0, [4, 10], 0, 0, 0, [16, 16], 0, 0, 0, [12, 14], 0, 0,
             0],
            [[0, 3], 0, 0, [3, 17], 0, 0, [6, 22], 0, 0, 0, 0, [4, 0], 0],
            [[0, 36], 0, 0, 0, 0, 0, 0, 0, [0, 12], 0, 0, 0, 0],
            [0, [0, 4], 0, 0, 0, [0, 14], 0, 0, 0, [0, 4], 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        tableauResolution = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None],
            [None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None],
            [None, None, 0, 0, 0, 0, None, 0, 0, None, 0, 0, None],
            [None, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, None],
            [None, 0, 0, 0, 0, None, 0, 0, 0, 0, None, None, None],
            [None, None, 0, 0, None, 0, 0, 0, None, 0, 0, None, None],
            [None, None, None, 0, 0, 0, 0, None, 0, 0, 0, 0, None],
            [None, None, 0, 0, 0, None, 0, 0, 0, None, 0, 0, None],
            [None, 0, 0, None, 0, 0, None, 0, 0, 0, 0, None, None],
            [None, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, None],
            [None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None]
        ]
        wrongMask = [
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", ""]
        ]
    if exempleProf:
        tailleGrille = 8
        tableauResolution = [
            [None, None, None, None, None, None, None, None, None],
            [None, 0, 0, None, None, 0, 0, 0, None],
            [None, 0, 0, None, 0, 0, 0, 0, None],
            [None, 0, 0, 0, 0, 0, None, None, None],
            [None, None, 0, 0, None, 0, 0, None, None],
            [None, None, None, 0, 0, 0, 0, 0, None],
            [None, 0, 0, 0, 0, None, 0, 0, None],
            [None, 0, 0, 0, None, None, 0, 0, None],
            [None, None, None, None, None, None, None, None, None]
        ]
        tableauIndice = [
            [0, [23, 0], [30, 0], 0, 0, [27, 0], [12, 0], [16, 0], 0],
            [[0, 16], 0, 0, 0, [17, 24], 0, 0, 0, 0],
            [[0, 17], 0, 0, [15, 29], 0, 0, 0, 0, 0],
            [[0, 35], 0, 0, 0, 0, 0, [12, 0], 0, 0],
            [0, [0, 7], 0, 0, [7, 8], 0, 0, [7, 0], 0],
            [0, [11, 0], [10, 16], 0, 0, 0, 0, 0, 0],
            [[0, 21], 0, 0, 0, 0, [0, 5], 0, 0, 0],
            [[0, 6], 0, 0, 0, 0, [0, 3], 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        wrongMask = [
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""]
        ]
    if medium:
        tailleGrille = 14
        tableauResolution = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, None, None],
            [None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
            [None, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, None],
            [None, None, None, 0, 0, 0, None, 0, 0, None, 0, 0, 0, None],
            [None, 0, 0, 0, 0, None, None, 0, 0, None, 0, 0, None, None],
            [None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
            [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, None],
            [None, None, 0, 0, None, 0, 0, None, None, 0, 0, 0, 0, None],
            [None, 0, 0, 0, None, 0, 0, None, 0, 0, 0, None, None, None],
            [None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, 0, None],
            [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, None],
            [None, None, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        ]
        tableauIndice = [
            [0, [23, 0], [13, 0], 0, [17, 0], [27, 0], [13, 0], [3, 0], [29, 0], 0, [3, 0], [37, 0], 0, 0],
            [[0, 16], 0, 0, [0, 32], 0, 0, 0, 0, 0, [14, 3], 0, 0, [11, 0], 0],
            [[0, 12], 0, 0, [11, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [[0, 11], 0, 0, 0, [23, 4], 0, 0, [28, 14], 0, 0, [23, 16], 0, 0, 0],
            [0, [7, 0], [44, 23], 0, 0, 0, [0, 7], 0, 0, [0, 10], 0, 0, 0, 0],
            [[0, 11], 0, 0, 0, 0, [31, 0], [29, 14], 0, 0, [10, 15], 0, 0, [13, 0], 0],
            [[0, 5], 0, 0, [7, 45], 0, 0, 0, 0, 0, 0, [0, 8], 0, 0, 0],
            [[0, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, [22, 4], 0, 0, 0],
            [0, [10, 11], 0, 0, [0, 6], 0, 0, 0, [14, 12], 0, 0, 0, 0, 0],
            [[0, 9], 0, 0, 0, [6, 12], 0, 0, [14, 19], 0, 0, 0, [9, 0], [21, 0], 0],
            [[0, 3], 0, 0, [12, 5], 0, 0, [14, 10], 0, 0, [4, 23], 0, 0, 0, 0],
            [[0, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, [0, 5], 0, 0, 0],
            [0, [0, 16], 0, 0, [0, 23], 0, 0, 0, 0, 0, [0, 11], 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        ]
        wrongMask = [
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        ]
    F([tableauResolution, tableauIndice])       # on exécute cette fonction pour mettre dans le mask les indices invalides
    printPrettyResultat([tableauResolution, tableauIndice]) # on affiche la grille initiale
    start_time = time.time()
    res = recuit([tableauResolution, tableauIndice])    # on démarre le recuit
    stop_time = time.time() - start_time
    printPrettyResultat(res)
    print(F(res), ' contraintes non respectées')
    print("temps  : ", stop_time, "s")


def recuit(X0):
    X = X0
    T = 1000  # température initiale
    Nt = 100  # nb d'itération
    step = 0
    while F(X) != 0 and step < 4000:    # la limitation du step est pour limiter le temps d'exécution à moins de 2 min a peu près
        for i in range(0, Nt):
            Y = voisin(X)
            dF = F(Y) - F(X)
            if accept(dF, T):
                X = Y
        step += 1
        T = decroissance(1, step)
    return X


def decroissance(t_min, step):
    return t_min / (1.8 * step**2)      # on diminue la température via une fonction quadratique


def voisin(x):  # fais en sorte qu'à une position random chacune des contraintes associées soient respectées en haut et à gauche
    newX = [[], x[1]]       # on copie notre grille
    for i in range(tailleGrille):
        newX[0].append(x[0][i].copy())
    i = random.randint(0, tailleGrille - 1)
    j = random.randint(0, tailleGrille - 1)
    hasZ = hasZero(x)
    while (hasZ and x[0][i][j] != 0) or x[0][i][j] is None:
        i = random.randint(0, tailleGrille - 1)
        j = random.randint(0, tailleGrille - 1)

    #find left start & contrainte
    leftStart = j
    pos = x[0][i][leftStart]
    while pos is not None:
        leftStart -= 1
        pos = x[0][i][leftStart]
    leftCtr = x[1][i][leftStart][1]

    #find whole line length
    lineLength = 1
    pos = x[0][i][leftStart + lineLength]
    while pos is not None:
        lineLength += 1
        pos = x[0][i][leftStart + lineLength]
    lineLength -= 1

    # pour toute la ligne on la remplis d'une façon qui satisfait toutes les contraintes si possible sinon on peut remplir quelque chose de faux
    nbStep = 0
    nbOk = 0                    # nombre de colonnes qui coincident bien avec la décomposition trouvée
    while nbStep < 100 and nbOk < (lineLength/5):  # on essaye de trouver la solution avec une marge d'erreur
        lineDecomposition = decomposition(leftCtr, lineLength)
        nbOk = 0
        for h in range(lineLength):
            contrainte = getConstraintsHaut(i, leftStart + h + 1, x)  # la contrainte d'une colonne
            colDecomposition = decomposition(contrainte[0], contrainte[1])
            if lineDecomposition[h] == colDecomposition[contrainte[2]]:     # si les deux contraintes on la bonne case et le bon nombre en commun
                nbOk += 1
                for l in range(len(colDecomposition)):
                    newX[0][l + contrainte[3]][leftStart + h + 1] = colDecomposition[l]  # on remets au bon endroit la colonne
            else:
                newX[0][i][leftStart + h+1] = lineDecomposition[h]                  # on remets au bon endroit la ligne
        nbStep += 1
    return newX


def getConstraintsHaut(i, j, tableau):
    it = i
    pos = tableau[0][it][j]
    while pos is not None:  # récupère la contrainte en haut
        it -= 1
        pos = tableau[0][it][j]
    contrainteHaut = tableau[1][it][j][0]
    it += 1
    pos = tableau[0][it][j]
    posStartHautX = it
    posStartHautY = j
    lengthHaut = 0
    while pos is not None:  # récupère la longueur du nombre demandé en haut
        lengthHaut += 1
        it += 1
        if it < tailleGrille:
            pos = tableau[0][it][j]
        else:
            pos = None

    offsetHaut = -(posStartHautX - i)  # sur une valeur à un endroit précis
    return [contrainteHaut, lengthHaut, offsetHaut, posStartHautX, posStartHautY]


def getConstraints(i, j, tableau):
    it = i
    pos = tableau[0][it][j]
    while pos is not None:  # récupère la contrainte en haut
        it -= 1
        pos = tableau[0][it][j]
    contrainteHaut = tableau[1][it][j][0]
    it += 1
    pos = tableau[0][it][j]
    posStartHautX = it
    posStartHautY = j
    lengthHaut = 0
    while pos is not None:  # récupère la longueur du nombre demandé en haut
        lengthHaut += 1
        it += 1
        if it < tailleGrille:
            pos = tableau[0][it][j]
        else:
            pos = None

    it = j
    pos = tableau[0][i][it]
    while pos is not None:  # récupère la contrainte à gauche
        it -= 1
        pos = tableau[0][i][it]
    contrainteGauche = tableau[1][i][it][1]
    it += 1
    pos = tableau[0][i][it]
    posStartGaucheX = i
    posStartGaucheY = it
    lengthGauche = 0
    while pos is not None:  # récupère la longueur du nombre demandé en haut
        lengthGauche += 1
        it += 1
        if it < tailleGrille:
            pos = tableau[0][i][it]
        else:
            pos = None

    offsetGauche = -(posStartGaucheY - j)  # les offsets sont utilisés pour accorder les décompositions
    offsetHaut = -(posStartHautX - i)  # sur une valeur à un endroit précis
    return [contrainteGauche, lengthGauche, offsetGauche, posStartGaucheX, posStartGaucheY, contrainteHaut, lengthHaut, offsetHaut, posStartHautX, posStartHautY]


def decomposition(num, subNum): # donne pour un nombre donné et un nombre de morceaux une décomposition avec des chiffres entre 1 et 9
    if subNum == 1:
        return num
    startNum = num
    startSubNum = subNum
    isGood = False
    res = []
    while not isGood:
        num = startNum
        subNum = startSubNum
        res = [0] * subNum
        cumulSum = 0
        subSection = 0
        max_random_number = min(9, startNum)
        while True:
            random_number = random.randint(1, max_random_number)
            res[subSection] = random_number
            cumulSum += random_number
            num -= random_number
            subSection += 1
            if cumulSum >= startNum:
                if cumulSum > startNum:
                    res[subSection-1] = cumulSum - startNum - (len(res) - subSection)

                i = subSection
                while i < len(res):
                    res[i] = 1
                    i += 1
                break
            if subSection == subNum - 1:
                random_number = num
                res[subSection] = random_number
                cumulSum += random_number
                break
        isGood = all(9 >= i >= 1 for i in res)  # on vérifie que la décomposition est bien entre 1 et 9
    return res


def F(x):  # calcul combien de contraintes sont non satisfaites
    energie = 0
    for i in range(0, tailleGrille):
        for j in range(0, tailleGrille):
            if x[1][i][j] != 0:
                energie = energie + isBadCalcul(x, i, j)        # on trouve un contrainte et on regarde les cases associées
    return energie


def isBadCalcul(tableau, i, j): # on resgarde si pour une case la contrainte du haut et de gauche sont non violés -> si oui on ajoute 1 au compteur nbMauvais par contrainte violée
    nbMauvais = 0
    indices = tableau[1][i][j]
    if isinstance(indices, list):
        if indices[0] != 0:     # contrainte du haut
            totalSum = 0
            it = i + 1    # un cran plus bas
            pos = tableau[0][it][j]
            while pos is not None:
                totalSum += pos
                it += 1
                if it < tailleGrille:
                    pos = tableau[0][it][j]
                else:
                    pos = None
            if totalSum != indices[0]:
                nbMauvais += 1
                wrongMask[i][j] = "W"
            else:
                wrongMask[i][j] = ""
        if indices[1] != 0:     # contrainte de gauche
            totalSum = 0
            it = j + 1    # un cran à droite
            pos = tableau[0][i][it]
            while pos is not None:
                totalSum += pos
                it += 1
                if it < tailleGrille:
                    pos = tableau[0][i][it]
                else:
                    pos = None
            if totalSum != indices[1]:
                nbMauvais += 1
                wrongMask[i][j] = "W"
            else:
                wrongMask[i][j] = ""
    return nbMauvais


def accept(dF, T):
    if dF > 0:
        A = math.exp(-dF/T)
        if A <= 0 or random.uniform(0, 1) >= A:
            return False
    return True


def hasZero(tableau):   # compte si il y a des 0 dans le tableau (valeur initiale)
    for i in range(len(tableau[0])):
        for j in range(len(tableau[0])):
            if tableau[0][i][j] == 0:
                return True
    return False


def printPrettyResultat(arr):  # print le tableau avec les indices
    output = ""
    tableau = arr[0]
    indices = arr[1]

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if tableau[i][j] is not None:  # c'est une case valeur
                value = str(tableau[i][j])
                if tableau[i][j] < 10:
                    value = "0" + value
                output = output + "   " + value + "  "
            else:  # c'est une case indice
                RESET = '\033[0m'
                RED = ""
                if wrongMask[i][j] != "":
                    RED = '\033[91m'
                if isinstance(indices[i][j], list):
                    indOne = str(indices[i][j][0])
                    indTwo = str(indices[i][j][1])
                    if indices[i][j][0] < 10:
                        indOne = "0" + indOne
                    if indices[i][j][1] < 10:
                        indTwo = "0" + indTwo
                else:
                    indOne = "00"
                    indTwo = "00"
                output = output + "|" + RED + indOne + "." + indTwo + RESET + "|"
        output = output + "\n"
    print("[↓→]")
    print(output)


if __name__ == '__main__':
    main()
