import random

class sudM():

    def __init__(self):
        self.gridG()

    def gridG(self): #Returns a suduko with some weird numbers inside
        self.m = [0 for y in range(81)]

    def pickR(self, row): #Returns the given row
        result = []
        for y in range(3):
            for x in range(3):
                result.append(self.m[y * 9 + x + int(row / 3) * 27 + (row % 3) * 3])
        return result

    def pickC(self, col): #Returns the given colunmn
        result = []
        for y in range(3):
            for x in range(3):
                result.append(self.m[y * 27 + x * 3 + col % 3 + int(col / 3) * 9])
        return result

    def idS(self, s): #Identifies which row, column and 3x3-square the square is in
        sq = int(s/9)
        r = int((s % 9) / 3) + int(sq / 3) * 3
        c = (s % 9) % 3 + (sq % 3) * 3

        return r, c, sq

    def checkS(self, s): #Checks which numbers are available
        r, c, sq = self.idS(s)
        rI = self.pickR(r)
        cI =  self.pickC(c)
        false = False
        print(rI, cI)
        true = []
        for n in range(0,10):
            if n in rI:
                pass
            elif n in cI:
                pass
            elif n in self.m[sq * 9: sq * 9 + 9]:
                pass
            else:
                true.append(n)
        return true

    def setS(self, s, inf):
        self.m[s] = int(inf)


