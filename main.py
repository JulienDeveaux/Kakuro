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
    print(F([tableauResolution, tableauIndice]))
    printResultat(tableauResolution)
    start_time = time.time()
    res = recuit([tableauResolution, tableauIndice])
    stop_time = time.time() - start_time
    printResultat(res)
    print(F(res), ' contraintes non respectées')
    print("temps  : ", stop_time, "s")


def recuit(X0):
    X = X0
    T = 1000  # plus c'est haut plus longtemps on peut remonter la courbe (diminue au fur et à mesure)
    Nt = 100  # nb d'iteration
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


def voisin(x):
    pos = random.randint(0, tailleGrille - 1)
    pos2 = random.randint(0, tailleGrille - 1)
    while x[0][pos][pos2] == "vide":
        pos = random.randint(0, tailleGrille - 1)
        pos2 = random.randint(0, tailleGrille - 1)
    x[0][pos][pos2] = random.randint(1, 9)
    return [x[0], x[1]]


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
