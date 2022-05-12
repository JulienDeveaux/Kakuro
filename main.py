import math
import random
import time


def main(tableauResolution=None, tableauIndice=None):
    global tailleGrille
    starter = True
    easy = False
    if starter:
        tailleGrille = 6  # contrainte [bas, droite]
        tableauIndice = [
            [[0, 0], [4, 0], [9, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 3], [0, 0], [0, 0], [24, 0], [0, 0], [0, 0]],
            [[0, 17], [0, 0], [0, 0], [0, 0], [17, 0], [0, 0]],
            [[0, 0], [0, 18], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [0, 16], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        ]
        tableauResolution = [
            ["vide", "vide", "vide", "vide", "vide", "vide"],
            ["vide", 0, 0, "vide", "vide", "vide"],
            ["vide", 0, 0, 0, "vide", "vide"],
            ["vide", "vide", 0, 0, 0, "vide"],
            ["vide", "vide", "vide", 0, 0, "vide"],
            ["vide", "vide", "vide", "vide", "vide", "vide"]
        ]
    if easy:
        tailleGrille = 11  # contrainte [bas, droite]
        tableauIndice = [
            [[0, 0], [4, 0], [22, 0], [0, 0], [0, 0], [25, 0], [9, 0], [0, 0], [0, 0], [17, 0], [19, 0], [0, 0]],
            [[0, 8], [0, 0], [0, 0], [8, 0], [0, 16], [0, 0], [0, 0], [16, 0], [16, 10], [0, 0], [0, 0], [16, 0]],
            [[0, 7], [0, 0], [0, 0], [0, 0], [16, 39], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [15, 23], [0, 0], [0, 0], [0, 0], [0, 0], [24, 17], [0, 0], [0, 0], [19, 12], [0, 0], [0, 0]],
            [[0, 7], [0, 0], [0, 0], [25, 6], [0, 0], [0, 0], [0, 0], [9, 13], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 27], [0, 0], [0, 0], [0, 0], [0, 0], [6, 21], [0, 0], [0, 0], [0, 0], [0, 0], [36, 0], [0, 0]],
            [[0, 0], [0, 16], [0, 0], [0, 0], [18, 9], [0, 0], [0, 0], [0, 0], [23, 17], [0, 0], [0, 0], [6, 0]],
            [[0, 0], [0, 0], [21, 16], [0, 0], [0, 0], [0, 0], [0, 0], [21, 20], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [4, 10], [0, 0], [0, 0], [0, 0], [16, 16], [0, 0], [0, 0], [0, 0], [12, 14], [0, 0], [0, 0]],
            [[0, 3], [0, 0], [0, 0], [3, 17], [0, 0], [0, 0], [6, 22], [0, 0], [0, 0], [0, 0], [0, 0], [4, 0]],
            [[0, 36], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 12], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 4], [0, 0], [0, 0], [0, 0], [0, 14], [0, 0], [0, 0], [0, 0], [0, 4], [0, 0], [0, 0]]
        ]
        tableauResolution = [
            ["vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide", "vide"],
            ["vide", 0, 0, "vide", "vide", 0, 0, "vide", "vide", 0, 0, "vide"],
            ["vide", 0, 0, 0, "vide", 0, 0, 0, 0, 0, 0, 0],
            ["vide", "vide", 0, 0, 0, 0, "vide", 0, 0, "vide", 0, 0],
            ["vide", 0, 0, "vide", 0, 0, 0, "vide", 0, 0, 0, "vide"],
            ["vide", 0, 0, 0, 0, "vide", 0, 0, 0, 0, "vide", "vide"],
            ["vide", "vide", 0, 0, "vide", 0, 0, 0, "vide", 0, 0, "vide"],
            ["vide", "vide", "vide", 0, 0, 0, 0, "vide", 0, 0, 0, 0],
            ["vide", "vide", 0, 0, 0, "vide", 0, 0, 0, "vide", 0, 0],
            ["vide", 0, 0, "vide", 0, 0, "vide", 0, 0, 0, 0, "vide"],
            ["vide", 0, 0, 0, 0, 0, 0, 0, "vide", 0, 0, 0],
            ["vide", "vide", 0, 0, "vide", "vide", 0, 0, "vide", "vide", 0, 0]]
    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if tableauResolution[i][j] == 0:
                tableauResolution[i][j] = random.randint(1, 9)
    printResultat(tableauResolution)
    print(getConstraints(2, 2, [tableauResolution, tableauIndice]))
    voisiny = voisin([tableauResolution, tableauIndice])
    printResultat(voisiny[0])
    start_time = time.time()
    res = recuit([tableauResolution, tableauIndice])
    stop_time = time.time() - start_time
    printResultat(res)
    print(F(res), ' contraintes non respectées')
    print("temps  : ", stop_time, "s")


def recuit(X0):
    X = X0
    T = 1000  # plus c'est haut plus longtemps on peut remonter la courbe (diminue au fur et à mesure)
    Nt = 100  # nb d'itération
    while F(X) != 0:
        for i in range(0, Nt):
            Y = voisin(X)
            dF = F(Y) - F(X)
            if accept(dF, T):
                X = Y
        T = decroissance(T)
        print(T)
        print(F(X))
    return X


def decroissance(T):
    value = (T - (T / 50) * 2)
    return value


def voisin(x):  # fais en sorte qu'à une position random chacune des contraintes associées soient respectées
    i = random.randint(0, tailleGrille - 1)
    j = random.randint(0, tailleGrille - 1)
    while x[0][i][j] == "vide":
        i = random.randint(0, tailleGrille - 1)
        j = random.randint(0, tailleGrille - 1)
    decompositions = getDecompositions(x, i, j)
    for h in range(len(decompositions[0][0])):          # on remet la décomposition dans les bonnes cases en hauteur
        x[0][decompositions[0][1]][decompositions[0][2] + h] = decompositions[0][0][h]
    for h in range(len(decompositions[1][0])):          # on remet la décomposition dans les bonnes cases en largeur
        x[0][decompositions[1][1] + h][decompositions[1][2]] = decompositions[1][0][h]
    return [x[0], x[1]]


def getConstraints(i, j, tableau):
    it = i
    pos = tableau[0][it][j]
    while pos != "vide":        # récupère la contrainte en haut
        it -= 1
        pos = tableau[0][it][j]
    contrainteHaut = tableau[1][it][j][0]
    it += 1
    pos = tableau[0][it][j]
    posStartHaut = [it, j]
    lengthHaut = 0
    while pos != "vide":        # récupère la longueur du nombre demandé en haut
        lengthHaut += 1
        it += 1
        pos = tableau[0][it][j]

    it = i
    pos = tableau[0][i][it]
    while pos != "vide":        # récupère la contrainte à gauche
        it -= 1
        pos = tableau[0][i][it]
    contrainteGauche = tableau[1][i][it][1]
    it += 1
    pos = tableau[0][i][it]
    posStartGauche = [i, it]
    lengthGauche = 0
    while pos != "vide":        # récupère la longueur du nombre demandé en haut
        lengthGauche += 1
        it += 1
        pos = tableau[0][i][it]

    offsetGauche = -(posStartGauche[1] - j)     # les offsets sont utilisés pour accorder les décompositions
    offsetHaut = -(posStartHaut[0] - i)         # sur une valeur à un endroit précis
    return [[contrainteGauche, lengthGauche, offsetGauche, posStartGauche],
            [contrainteHaut, lengthHaut, offsetHaut, posStartHaut]]


def getDecompositions(tableau, i, j):
    contraintes = getConstraints(i, j, tableau)
    decomposition1 = decomposition(contraintes[0][0], contraintes[0][1])
    decomposition2 = decomposition(contraintes[1][0], contraintes[1][1])
    positionDansCtr1 = contraintes[0][2]
    positionDansCtr2 = contraintes[1][2]
    while(decomposition1[positionDansCtr1] != decomposition2[positionDansCtr2]):    # fais en sorte qu'a la position random choisie dans voisin les deux décompositions aient la même valeur
        decomposition1 = decomposition(contraintes[0][0], contraintes[0][1])
        decomposition2 = decomposition(contraintes[1][0], contraintes[1][1])
    startingPoint1 = contraintes[0][3][0]
    startingPoint2 = contraintes[1][3][0]
    endingPoint1 = contraintes[0][3][1]
    endingPoint2 = contraintes[1][3][1]
    return [[decomposition1, startingPoint1, endingPoint1], [decomposition2, startingPoint2, endingPoint2]]


def decomposition(num, subNum):
    res = [None] * subNum
    cumulSum = 0
    subSection = 0
    max_random_number = int(num / subNum)
    while True:
        random_number = random.randint(1, max_random_number)
        res[subSection] = random_number
        cumulSum += random_number
        num -= random_number
        subSection += 1
        if subSection == subNum - 1:
            random_number = num
            res[subSection] = random_number
            cumulSum += random_number
            break
    return res


def F(x):  # calcul combien de contraintes son non satisfaites
    energie = 0
    for i in range(0, tailleGrille):
        for j in range(0, tailleGrille):
            if x[1][i][j] != [0, 0]:
                energie = energie + isBadCalcul(x, i, j)
    return energie


def isBadCalcul(tableau, i, j):
    nbMauvais = 0
    indices = tableau[1][i][j]
    if indices[0] != 0:
        calcul = 0
        it = j - 1
        pos = tableau[0][it][j]
        while pos != "vide":
            calcul += pos
            it = it + 1
            if it >= len(tableau[0][it]) - 1:
                pos = "vide"
            else:
                pos = tableau[0][it][j]
        if calcul != indices[0]:
            nbMauvais = nbMauvais + 1
    if indices[1] != 0:
        calcul = 0
        it = j + 1
        pos = tableau[0][i][it]
        while pos != "vide":
            calcul += pos
            it = it + 1
            if it >= len(tableau[0][i]) - 1:
                pos = "vide"
            else:
                pos = tableau[0][i][it]
        if calcul != indices[1]:
            nbMauvais = nbMauvais + 1
    return nbMauvais


def accept(dF, T):
    if dF > 0:
        A = math.exp(-dF / T)
        if random.uniform(0, 1) >= A:
            return False
    return True


def printResultat(tableau):
    output = ""

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if tableau[i][j] != "vide":
                output = output + " " + str(tableau[i][j]) + " "
            else:
                output = output + " □ "
        output = output + "\n"
    print(output)


if __name__ == '__main__':
    main()