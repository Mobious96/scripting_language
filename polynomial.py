class Polynomial:
    #self.coeffs = []

    #Delete first N zeros as Polynomial([0,0,1,2]) same as Polynomial([1,2])
    def fixZeros(self):
        for k,v in enumerate(self.coeffs):  # 1 2 3 4 -> 1x^3 + 2x^2 + 3x + 4, but coeffs[0] = 4, coeffs[1] = 3, coeffs[i] = arg(x^i)
            if v != 0:
                del self.coeffs[:k]
                break
        if len(self.coeffs) == 0:   #Polinomial ALWAYS have 0 on the end? It's needed to be able to work with object even if it's empty. For example, to print polynomial, to __add__
            self.coeffs.append(0)
        return

    def isEmpty(self):
        return not len(self.coeffs) #0 - False, any other - True

    def __init__(self,_coeffs):
        self.coeffs = []
        if isinstance(_coeffs, (int)):
            self.coeffs.append(_coeffs)
            return
        if isinstance(_coeffs, Polynomial):
            for v in _coeffs:
                self.coeffs[v] = _coeffs[v]
            return
        if not isinstance(_coeffs, (list, tuple)):
            raise TypeError("Supported types for creating polynomial: list, tuple, int, Polynomial")
        else:
            for k,v in enumerate(_coeffs): #delete first N zeros
                if v != 0:
                    self.coeffs = _coeffs[k:]
                    return
                if self.isEmpty():  # Polinomial ALWAYS have 0 on the end? It's needed to be able to work with object even if it's empty. For example, to print polynomial, to __add__
                    self.coeffs.append(0)

    #1,2,3,4 = x^3 + 2x^2 + 3x + 4
    def __str__(self):
        text = ""
        #For X with max degree there are special rule to represent: "-2x^n_+_...". "-" without spaces
        if (len(self.coeffs) > 1):
            #x^n
            text = text + (("-" if self.coeffs[0] < 0 else "") + (str(abs(self.coeffs[0])) if abs(self.coeffs[0]) != 1 else "") + "x^" + str(len(self.coeffs) - 1) if self.coeffs[0] != 0 else "")
            #[x^(n-1)..x^2]
            for k,v in enumerate(self.coeffs[1: -2]):
                if v != 0:
                    text = text + (" - " if v < 0 else " + ") + (str(abs(v)) if abs(v) != 1 else "") + "x^"+str(len(self.coeffs)-k - 2)
            #x^1
            text = text + (((" + " if self.coeffs[-2] > 0 else " - ") + (str(abs(self.coeffs[-2])) if (abs(self.coeffs[-2]) != 1) else "") + "x") if self.coeffs[-2] != 0 else "")
            #x^0
            text = text + (((" + " if self.coeffs[-1] > 0 else " - ") + str(abs(self.coeffs[-1]))) if self.coeffs[-1] != 0 else "")
        else:
            text = text + (("" if self.coeffs[0] >= 0 else "-") + str(abs(self.coeffs[0])))
        return text

    def __repr__(self):
        return "Polynomial("+str(self.coeffs)+")"

    def __eq__(self, other):
        if not isinstance(other, Polynomial): #How can I check whenether can I cast type(other) to Polinomlial or not. Will it cost more (time/memory( than just checking and hardcoding?
            if not isinstance(other, int):
                raise TypeError("Can't compare " + str(type(self)) + " with " + str(type(other)))
            else:
                return self.coeffs[0] == other
        else:
            return self.coeffs == other.coeffs

    def __len__(self):
        return len(self.coeffs)

    def __add__(self, other):
        if not isinstance(other, (list, tuple, int, Polynomial)):
            TypeError("Supported types to add: list, tuple, int, Polynomial")
        if isinstance(other, Polynomial):
            if self.isEmpty():
                self.coeffs = other.coeffs[:]
                return
            if len(self) >= len(other):
                for k,v in enumerate(reversed(other.coeffs)):
                    self.coeffs[-(k+1)] += v
            else:
                for k,v in enumerate(reversed(self.coeffs)): #process same degree
                    self.coeffs[-(k+1)] += other.coeffs[-(k+1)]
                #copy new degree coeffs
                self.coeffs[0:0] = other.coeffs[:len(other.coeffs) - len(self.coeffs)] #https://www.geeksforgeeks.org/python-insert-list-in-another-list/
        elif isinstance(other, int):
            if self.isEmpty():
                self = Polynomial(other)
                return
            else:
                self.coeffs[-1] += other
        else:
            TypeError("Error: how did you get here you cheeky bastard?")
        self.fixZeros()
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return

    def __rmul__(self, other):
        return self.__mul__(other)