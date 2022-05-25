import random


class kakuroBoard:

    def __init__(self, indices, valeurs, mode):     #0 new, 1 copy -> (array avec tout, copy, mode)
        if mode == 0:
            self.indices = indices
            self.valeurs = valeurs
            self.copy = [[], indices]
            self.tailleGrille = len(self.indices)
            self.wrongMask = self.genMask()
        else:
            self.valeurs = indices[0]
            self.indices = indices[1]
            self.copy = valeurs
            self.wrongMask = mode
            self.tailleGrille = len(self.indices)

    def setWholeValues(self, values):
        self.valeurs = values

    def setCopy(self, copy):
        self.copy = copy

    def setValue(self, x, y, val):
        self.valeurs[x][y] = val

    def getValue(self, x, y):
        return self.valeurs[x][y]

    def getValueLine(self, x):
        return self.valeurs[x]

    def getIndice(self, x, y, w):
        return self.indices[x][y][w]

    def getIndiceTwin(self, x, y):
        return self.indices[x][y]

    def genMask(self):
        res = []
        for i in range(self.tailleGrille):
            toAppend = []
            for j in range(self.tailleGrille):
                toAppend.append("")
            res.append(toAppend)
        return res

    def isBadCalcul(self, i, j):
        nbMauvais = 0
        if isinstance(self.indices[i][j], list):
            if self.indices[i][j][0] != 0:  # contrainte du haut
                totalSum = 0
                it = i + 1  # un cran plus bas
                pos = self.valeurs[it][j]
                while pos is not None:
                    totalSum += pos
                    it += 1
                    if it < self.tailleGrille:
                        pos = self.valeurs[it][j]
                    else:
                        pos = None
                if totalSum != self.indices[i][j][0]:
                    nbMauvais += 1
                    self.wrongMask[i][j] = "W"
                else:
                    self.wrongMask[i][j] = ""
            if self.indices[i][j][1] != 0:  # contrainte de gauche
                totalSum = 0
                it = j + 1  # un cran à droite
                pos = self.valeurs[i][it]
                while pos is not None:
                    totalSum += pos
                    it += 1
                    if it < self.tailleGrille:
                        pos = self.valeurs[i][it]
                    else:
                        pos = None
                if totalSum != self.indices[i][j][1]:
                    nbMauvais += 1
                    self.wrongMask[i][j] = "W"
                else:
                    self.wrongMask[i][j] = ""
        return nbMauvais

    def hasZero(self):
        for i in range(self.tailleGrille):
            for j in range(self.tailleGrille):
                if self.valeurs[i][j] == 0:
                    return True
        return False

    def howManyZero(self):
        res = 0
        for i in range(len(self.valeurs)):
            for j in range(len(self.valeurs)):
                if self.valeurs[i][j] == 0:
                    res += 1
        return res

    def getDecompositions(self, x, y):
        it = x
        pos = self.valeurs[it][y]
        while pos is not None:  # récupère la contrainte en haut
            it -= 1
            pos = self.valeurs[it][y]
        contrainteHaut = self.indices[it][y][0]
        it += 1
        pos = self.valeurs[it][y]
        posStartHautX = it
        posStartHautY = y
        lengthHaut = 0
        while pos is not None:  # récupère la longueur du nombre demandé en haut
            lengthHaut += 1
            it += 1
            if it < self.tailleGrille:
                pos = self.valeurs[it][y]
            else:
                pos = None

        it = y
        pos = self.valeurs[x][it]
        while pos is not None:  # récupère la contrainte à gauche
            it -= 1
            pos = self.valeurs[x][it]
        contrainteGauche = self.indices[x][it][1]
        it += 1
        pos = self.valeurs[x][it]
        posStartGaucheX = x
        posStartGaucheY = it
        lengthGauche = 0
        while pos is not None:  # récupère la longueur du nombre demandé en haut
            lengthGauche += 1
            it += 1
            if it < self.tailleGrille:
                pos = self.valeurs[x][it]
            else:
                pos = None

        offsetGauche = -(posStartGaucheY - y)  # les offsets sont utilisés pour accorder les décompositions
        offsetHaut = -(posStartHautX - x)  # sur une valeur à un endroit précis
        decomposition1 = self.decomposition(contrainteGauche, lengthGauche)
        decomposition2 = self.decomposition(contrainteHaut, lengthHaut)
        positionDansCtr1 = offsetGauche
        positionDansCtr2 = offsetHaut
        if decomposition1[positionDansCtr1] == decomposition2[positionDansCtr2]:  # fais en sorte qu'a la position random choisie dans voisin les deux décompositions aient la même valeur
            startingPoint1 = posStartGaucheX
            endingPoint1 = posStartGaucheY
            startingPoint2 = posStartHautX
            endingPoint2 = posStartHautY
            res = [decomposition1, startingPoint1, endingPoint1, decomposition2, startingPoint2, endingPoint2]
        else:
            res = None
        return res

    def decomposition(self, num, subNum):
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
                        res[subSection - 1] = cumulSum - startNum - (len(res) - subSection)

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
            isGood = all(9 >= i >= 1 for i in res)  # TODO do better than this
        return res

    def print(self):
        output = "[↓→]\n"

        for i in range(self.tailleGrille):
            for j in range(self.tailleGrille):
                if self.valeurs[i][j] is not None:  # c'est une case valeur
                    value = str(self.valeurs[i][j])
                    if self.valeurs[i][j] < 10:
                        value = "0" + value
                    output = output + "   " + value + "  "
                else:  # c'est une case indice
                    RESET = '\033[0m'
                    RED = ""
                    if self.wrongMask[i][j] != "":
                        RED = '\033[91m'
                    if isinstance(self.indices[i][j], list):
                        indOne = str(self.indices[i][j][0])
                        indTwo = str(self.indices[i][j][1])
                        if self.indices[i][j][0] < 10:
                            indOne = "0" + indOne
                        if self.indices[i][j][1] < 10:
                            indTwo = "0" + indTwo
                    else:
                        indOne = "00"
                        indTwo = "00"
                    output = output + "|" + RED + indOne + "." + indTwo + RESET + "|"
            output = output + "\n"
        print(output)
