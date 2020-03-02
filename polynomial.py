#Load numpy and make optimization https://habr.com/ru/post/455722/


class Polynomial:
    #self.coeffs = []

    def __init__(self,_coeffs):
        self.coeffs = []
        if isinstance(_coeffs, (int)):
            self.coeffs.append(_coeffs)
            return
        if not isinstance(_coeffs, (list, tuple, set, int)):
            raise TypeError("Supported types for creating polynomial: list, tuple, set")
        badZerosExists = True #remove first N zeros since they are usless, e.g. [0,0,0,1,2] -> x + 2 same as [1,2]
        #index = _coeffs.index(not 0);
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

        if (len(self.coeffs) > 1):
            #x^n
            text = text + (("-" if self.coeffs[0] < 0 else "") + (str(abs(self.coeffs[0])) if abs(self.coeffs[0]) != 1 else "") + "x^" + str(len(self.coeffs) - 1) if self.coeffs[0] != 0 else "")
            #print("text1:" + text)
            #[x^(n-1)..x^2]
            for k,v in enumerate(self.coeffs[1: -2]):
                if v != 0:
                    text = text + (" - " if v < 0 else " + ") + (str(abs(v)) if abs(v) != 1 else "") + "x^"+str(len(self.coeffs)-k - 2)
                    #print("text:"+k+" " + text)
            #x^1
            text = text + (((" + " if self.coeffs[-2] > 0 else " - ") + (str(abs(self.coeffs[-2])) if (abs(self.coeffs[-2]) != 1) else "") + "x") if self.coeffs[-2] != 0 else "")
            #x^0
            text = text + (((" + " if self.coeffs[-1] > 0 else " - ") + str(abs(self.coeffs[-1]))) if self.coeffs[-1] != 0 else "")
        else:
            text = text + ((("" if self.coeffs[-1] > 0 else "-") + str(abs(self.coeffs[-1]))) if self.coeffs[-1] != 0 else "")
        return text

    def __repr__(self):
        return "Polynomial("+str(self.coeffs)+")"

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            TypeError("Can't compare " + str(type(self)) + " with " + str(type(other)))
        else:
            return self.coeffs == other.coeffs

    def __len__(self):
        return len(self.coeffs)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if len(self) > len(other):
                for k,v in enumerate(other.coeffs):
                    self.coeffs[len(self.coeffs) - k - 1] += other.coeffs[len(self.coeffs) - k - 1] #since 1,2,3,4 means x^3 + 2x^2 + 3x^1 + 4 we start from the end
            else:
                for k,v in enumerate(self.coeffs):
                    self.coeffs[len(self.coeffs) - k - 1] += other.coeffs[len(self.coeffs) - k - 1]
        return self