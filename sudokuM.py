import random

class sudM():

    def gridG(self): #Returns a suduko with some weird numbers inside
        self.m = [[[str(varx+vary+whole) for varx in range(3)] for vary in range(3)] for whole in range(9)]

    def pickR(self, row): #Returns the given row
        result = []
        l = {1 : [0,3], 2 : [0,3], 3 : [0,3], 4 : [3,6], 5 : [3, 6], 6 : [3, 6], 7 : [6, 9], 8 : [6, 9], 9 : [6, 9]}
        for outL in self.m[l[row][0]:l[row][1]]:
            result.append(self.m[outL][row])
        return result

    def pickC(self, col): #Returns the given colunmn
        result = []
        for outC in range(0,9,3):
            for outIC in self.m:
                result.append(outIC[int(col/3)][col%3])
        return result


    def idS(self, s): #Identifies which row, column and 3x3-square the square is in
        r = int(s[0]/3) * 3 + s[1]
        c = (s[0]%3 * 3) + s[2]
        sq = sudM.m[s[0]]
        return r, c, sq

    def checkS(self, s): #Checks which numbers are available
        r, c = sudM.idS(s)
        rI = sudM.pickR(r)
        cI =  sudM.pickC(c)
        false = False
        true = []
        for n in range(1,11):
            if n in rI:
                false = False
            elif n in cI:
                false = False
            elif n in m[s[0]]:
                false = False
            else:
                true.append(n)
        return true

    def switchP(self, s):
        r, c, sq = sudM.idS(s)
        val = sudM.m[s[0]][s[1]][s[2]]


