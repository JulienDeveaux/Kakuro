import math
import random
import time

from kakuroBoard import kakuroBoard


def main():
    starter = True
    easy = False
    exempleProf = False
    medium = False
    tableauIndice = []
    tableauResolution = []
    if starter:
        tableauIndice = [
            [0, [4, 0], [9, 0], 0, 0, 0],
            [[0, 3], 0, 0, [24, 0], 0, 0],
            [[0, 17], 0, 0, 0, [17, 0], 0],
            [0, [0, 18], 0, 0, 0, 0],
            [0, 0, [0, 16], 0, 0, 0]
        ]
        tableauResolution = [
            [None, None, None, None, None, None],
            [None, 0, 0, None, None, None],
            [None, 0, 0, 0, None, None],
            [None, None, 0, 0, 0, None],
            [None, None, None, 0, 0, None]
        ]
    if easy:
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
            [0, [0, 4], 0, 0, 0, [0, 14], 0, 0, 0, [0, 4], 0, 0, 0]
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
            [None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None]
        ]
    if exempleProf:
        tableauResolution = [
            [None, None, None, None, None, None, None, None],
            [None, 0, 0, None, None, 0, 0, 0],
            [None, 0, 0, None, 0, 0, 0, 0],
            [None, 0, 0, 0, 0, 0, None, None],
            [None, None, 0, 0, None, 0, 0, None],
            [None, None, None, 0, 0, 0, 0, 0],
            [None, 0, 0, 0, 0, None, 0, 0],
            [None, 0, 0, 0, None, None, 0, 0]
        ]
        tableauIndice = [
            [0, [23, 0], [30, 0], 0, 0, [27, 0], [12, 0], [16, 0]],
            [[0, 16], 0, 0, 0, [17, 24], 0, 0, 0],
            [[0, 17], 0, 0, [15, 29], 0, 0, 0, 0],
            [[0, 35], 0, 0, 0, 0, 0, [12, 0], 0],
            [0, [0, 7], 0, 0, [7, 8], 0, 0, [7, 0]],
            [0, [11, 0], [10, 16], 0, 0, 0, 0, 0],
            [[0, 21], 0, 0, 0, 0, [0, 5], 0, 0],
            [[0, 6], 0, 0, 0, 0, [0, 3], 0, 0]
        ]
    if medium:
        tableauResolution = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0, None],
            [None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [None, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0],
            [None, None, None, 0, 0, 0, None, 0, 0, None, 0, 0, 0],
            [None, 0, 0, 0, 0, None, None, 0, 0, None, 0, 0, None],
            [None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0],
            [None, None, 0, 0, None, 0, 0, None, None, 0, 0, 0, 0],
            [None, 0, 0, 0, None, 0, 0, None, 0, 0, 0, None, None],
            [None, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, 0],
            [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0],
            [None, None, 0, 0, None, 0, 0, 0, 0, 0, None, 0, 0]
        ]
        tableauIndice = [
            [0, [23, 0], [13, 0], 0, [17, 0], [27, 0], [13, 0], [3, 0], [29, 0], 0, [3, 0], [37, 0], 0],
            [[0, 16], 0, 0, [0, 32], 0, 0, 0, 0, 0, [14, 3], 0, 0, [11, 0]],
            [[0, 12], 0, 0, [11, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [[0, 11], 0, 0, 0, [23, 4], 0, 0, [28, 14], 0, 0, [23, 16], 0, 0],
            [0, [7, 0], [44, 23], 0, 0, 0, [0, 7], 0, 0, [0, 10], 0, 0, 0],
            [[0, 11], 0, 0, 0, 0, [31, 0], [29, 14], 0, 0, [10, 15], 0, 0, [13, 0]],
            [[0, 5], 0, 0, [7, 45], 0, 0, 0, 0, 0, 0, [0, 8], 0, 0],
            [[0, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, [22, 4], 0, 0],
            [0, [10, 11], 0, 0, [0, 6], 0, 0, 0, [14, 12], 0, 0, 0, 0],
            [[0, 9], 0, 0, 0, [6, 12], 0, 0, [14, 19], 0, 0, 0, [9, 0], [21, 0]],
            [[0, 3], 0, 0, [12, 5], 0, 0, [14, 10], 0, 0, [4, 23], 0, 0, 0],
            [[0, 45], 0, 0, 0, 0, 0, 0, 0, 0, 0, [0, 5], 0, 0],
            [0, [0, 16], 0, 0, [0, 23], 0, 0, 0, 0, 0, [0, 11], 0, 0]
        ]
    board = kakuroBoard(tableauIndice, tableauResolution, 0)
    F(board)
    board.print()
    start_time = time.time()
    res = recuit(board)
    stop_time = time.time() - start_time
    F(res)
    res.print()
    print(F(res), ' contraintes non respectées')
    print("temps  : ", stop_time, "s")


def recuit(X0):
    X = X0
    T = 1000  # plus c'est haut plus longtemps on peut remonter la courbe (diminue au fur et à mesure)
    Nt = 100  # nb d'itération
    prevSize = 150
    prevX = [0] * prevSize
    it = 0
    while F(X) != 0:
        for i in range(0, Nt):
            Y = voisin(X)
            dF = F(Y) - F(X)
            if accept(dF, T):
                X = Y
        """if all((x != 0 and x == prevX[0]) for x in prevX):
            T += 0.4
            prevX = [0] * prevSize
            print(F(X))
        else:
            prevX[it] = F(X)
            if it == prevSize - 1:
                it = 0
            else:
                it += 1
            T = decroissance(T)"""
        #print(F(X), " ", T)
        T = decroissance(T)
    return X


def decroissance(T):
    value = (T - (T / 50) * 2)
    return value


def voisin(x):  # fais en sorte qu'à une position random chacune des contraintes associées soient respectées
    newX = []
    for i in range(x.tailleGrille):
        newX.append(x.getValueLine(i).copy())
    i = random.randint(0, x.tailleGrille - 1)
    j = random.randint(0, x.tailleGrille - 1)
    hasZ = x.hasZero()
    while (hasZ and x.getValue(i, j) != 0) or x.getValue(i, j) is None:
        i = random.randint(0, x.tailleGrille - 1)
        j = random.randint(0, x.tailleGrille - 1)
    decompositions = x.getDecompositions(i, j)
    if isinstance(decompositions, list):
        for h in range(len(decompositions[0])):
            newX[decompositions[1]][decompositions[2] + h] = decompositions[0][h]
        for h in range(len(decompositions[3])):
            newX[decompositions[4] + h][decompositions[5]] = decompositions[3][h]
    x.setWholeValues(newX)
    return x


def F(x):  # calcul combien de contraintes son non satisfaites
    energie = 0
    for i in range(0, x.tailleGrille):
        for j in range(0, x.tailleGrille):
            if x.getIndiceTwin(i, j) != 0:
                energie = energie + x.isBadCalcul(i, j)        # on trouve un contrainte et on regarde les cases associées
    return energie


def accept(dF, T):
    if dF > 0:
        A = math.exp(-dF / T)
        if random.uniform(0, 1) >= A:
            return False
    return True


if __name__ == '__main__':
    main()
