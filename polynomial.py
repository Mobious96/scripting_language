#Load numpy and make optimization https://habr.com/ru/post/455722/


class Polynomial:
    #self.coeffs = []

    def __init__(self,_coeffs):
        if not isinstance(_coeffs, (list, tuple, set)):
            raise TypeError("Supported types for creating polynomial: list, tuple, set")
        badZerosExists = True #remove first N zeros since they are usless, e.g. [0,0,0,1,2] -> x + 2 same as [1,2]
        #index = _coeffs.index(not 0);
        self.coeffs = []
        for v in _coeffs: #1 2 3 4 -> 1x^3 + 2x^2 + 3x + 4, but coeffs[0] = 4, coeffs[1] = 3, coeffs[i] = arg(x^i)
            if(badZerosExists):
                if v != 0:
                    badZerosExists = False
                    self.coeffs.append(int(v)) #checks whenever can cast to int or not
                else:
                    continue
            else:
                self.coeffs.append(int(v)) #checks whenever can cast to int or not

    #1,2,3,4 = x^3 + 2x^2 + 3x + 4
    def __str__(self):
        text = ""
        #print("text:" + text)
        #For X with max degree there are special rule to represent: "-2x^n_+_...". "-" without spaces
        #x^n
        text = text + (("-" if self.coeffs[0] < 0 else "") + (str(abs(self.coeffs[0])) if abs(self.coeffs[0]) != 1 else "") + "x^" + str(len(self.coeffs) - 1) if self.coeffs[0] != 0 else "")
        for k,v in enumerate(self.coeffs[1: -2]):
            if v != 0:
                text = text + (" - " if v < 0 else " + ") + (str(abs(v)) if abs(v) != 1 else "") + "x^"+str(len(self.coeffs)-k - 2)
        #x^1
        text = text + (((" + " if self.coeffs[-2] > 0 else " - ") + (str(abs(self.coeffs[-2])) if ((abs(self.coeffs[-2]) != 1) or (self.coeffs[-2] != 0)) else "") + "x") if self.coeffs[-2] != 0 else "")
        #x^0
        text = text + ((" + " if self.coeffs[-1] > 0 else " - ") + (str(abs(self.coeffs[-1])) if ((abs(self.coeffs[-1]) != 1) or (self.coeffs[-1] != 0)) else "") if self.coeffs[-1] != 0 else "")
        return text

