class Polynomial:
    #self.coeffs = []

    #Delete first N zeros as Polynomial([0,0,1,2]) same as Polynomial([1,2])
    def fixZeros(self):
        for k,v in enumerate(self.coeffs):  # 1 2 3 4 -> 1x^3 + 2x^2 + 3x + 4, but coeffs[0] = 4, coeffs[1] = 3, coeffs[i] = arg(x^i)
            if v != 0:
                del self.coeffs[:k]
                return
        if k == len(self.coeffs)-1:
            del self.coeffs[:]
            self.coeffs.append(0)
        # if len(self.coeffs) == 0:   #Polinomial ALWAYS have 0 on the end? It's needed to be able to work with object even if it's empty. For example, to print polynomial, to __add__
        #     self.coeffs.append(0)
        return

    def isEmpty(self):
        if (len(self.coeffs) == 0):
            return True
        elif len(self.coeffs) == 1:
            if (self.coeffs[0] == 0):
                return True
        return False

    def __init__(self,_coeffs):
        self.coeffs = []
        if isinstance(_coeffs, (int)):
            self.coeffs.append(_coeffs)
            return
        if isinstance(_coeffs, Polynomial):
            self.coeffs = _coeffs.coeffs[:]
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
        if (len(self.coeffs) > 2):
            #x^n
            text = text + (("-" if self.coeffs[0] < 0 else "") + (str(abs(self.coeffs[0])) if abs(self.coeffs[0]) != 1 else "") + "x^" + str(len(self.coeffs) - 1) if self.coeffs[0] != 0 else "")
            #[x^(n-1)..x^2]
            for k,v in enumerate(self.coeffs[1: -2]):
                if v != 0:
                    text = text + (" - " if v < 0 else " + ") + (str(abs(v)) if abs(v) != 1 else "") + "x^"+str(len(self.coeffs)-k - 2)
            # x^1
            text = text + (((" + " if self.coeffs[-2] > 0 else " - ") + (str(abs(self.coeffs[-2])) if (abs(self.coeffs[-2]) != 1) else "") + "x") if self.coeffs[-2] != 0 else "")
            # x^0
            text = text + (((" + " if self.coeffs[-1] > 0 else " - ") + str(abs(self.coeffs[-1]))) if self.coeffs[-1] != 0 else "")
        #x^1
        elif (len(self.coeffs) == 2):
            text = text + ((("" if self.coeffs[-2] > 0 else " - ") + (str(abs(self.coeffs[-2])) if (abs(self.coeffs[-2]) != 1) else "") + "x") if self.coeffs[-2] != 0 else "")
            #x^0
            text = text + (((" + " if self.coeffs[-1] > 0 else " - ") + str(abs(self.coeffs[-1]))) if self.coeffs[-1] != 0 else "")
        elif (len(self.coeffs) == 1):
            text = text + (("" if self.coeffs[0] >= 0 else "-") + str(abs(self.coeffs[0])))
        else:
            Exception("Error: len(self.coeffs) == " + len(self.coeffs))
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
        if not isinstance(other, (int, Polynomial)):
            raise TypeError("Supported types to add: int, Polynomial")
        if isinstance(other, Polynomial):
            if self.isEmpty():
                self.coeffs = other.coeffs[:]
            if len(self) >= len(other):
                for k,v in enumerate(reversed(other.coeffs)):
                    self.coeffs[-(k+1)] += v
            else:
                for k,v in enumerate(reversed(self.coeffs)): #process same degree
                    self.coeffs[-(k+1)] += other.coeffs[-(k+1)]
                #copy new degree coeffs
                self.coeffs[0:0] = other.coeffs[:len(other.coeffs) - len(self.coeffs)] #https://www.geeksforgeeks.org/python-insert-list-in-another-list/
        elif isinstance(other, int):
            self.coeffs[-1] += other
        else:
            raise TypeError("Error: how did you get here you cheeky bastard?")
        self.fixZeros()
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, (int, Polynomial)):
            raise TypeError("Supported types to sub: int, Polynomial")
        buf = Polynomial(self)
        if isinstance(other, Polynomial):
            if buf.isEmpty():
                #buf.coeffs = (other.coeffs[:]*(-1))
                buf.coeffs = [i*(-1) for i in other.coeffs[:]]
            if len(buf) >= len(other):
                for k, v in enumerate(reversed(other.coeffs)):
                    buf.coeffs[-(k + 1)] -= v
            else:
                for k, v in enumerate(reversed(buf.coeffs)):  # process same degree
                    buf.coeffs[-(k + 1)] -= other.coeffs[-(k + 1)]
                # copy new degree coeffs
                #buf.coeffs[0:0] = (other.coeffs[:len(other.coeffs) - len(buf.coeffs)])*(-1)
                buf.coeffs[0:0] = [i * (-1) for i in other.coeffs[:len(other.coeffs) - len(buf.coeffs)]]
        elif isinstance(other, int):
            if buf.isEmpty():
                buf = (Polynomial(other * (-1)))
            else:
                buf.coeffs[-1] -= other
        else:
            raise TypeError("Error: how did you get here you cheeky bastard?")
        buf.fixZeros()
        return buf

    def __rsub__(self, other):
        if not isinstance(other, (int, Polynomial)):
            raise TypeError("Supported types to sub: list, tuple, int, Polynomial")
        buf = Polynomial(self * (-1))
        if isinstance(other, Polynomial):
            if buf.isEmpty():
                buf.coeffs = other.coeffs[:]
            if len(buf) >= len(other):
                for k, v in enumerate(reversed(other.coeffs)):
                    buf.coeffs[-(k + 1)] += v
            else:
                for k, v in enumerate(reversed(buf.coeffs)):  # process same degree
                    buf.coeffs[-(k + 1)] += other.coeffs[-(k + 1)]
                # copy new degree coeffs
                buf.coeffs[0:0] = other.coeffs[:len(other.coeffs) - len(
                    buf.coeffs)]  # https://www.geeksforgeeks.org/python-insert-list-in-another-list/
        elif isinstance(other, int):
            buf.coeffs[-1] += other
        else:
            raise TypeError("Error: how did you get here you cheeky bastard?")
        buf.fixZeros()
        return buf

    def __mul__(self, other):
        if not isinstance(other, (int, Polynomial)):
            raise TypeError("Supported types to add: list, tuple, int, Polynomial")
        if isinstance(other, int):
            buf = Polynomial([i * other for i in self.coeffs])
        if isinstance(other, Polynomial):
            buf = Polynomial(self)
            for k,v in enumerate(reversed(other.coeffs)):
                buf.coeffs = [i * v for i in buf.coeffs]


        buf.fixZeros()
        return buf

    def __rmul__(self, other):
        return self.__mul__(other)