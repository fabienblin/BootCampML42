class Vector:
    def __init__(self, values=None):
        self.tab: list = []
        self.size: int = 0

        if values is not None\
           and type(values) is list\
           and all(isinstance(v, float) for v in values):
            self.tab = values
            self.size = len(self.tab)
        elif values is not None\
             and type(values) is int\
             and values >= 0:
            for i in range(0, values):
                self.tab.append(float(i))
            self.size = len(self.tab)
        elif values is not None\
             and type(values) is tuple\
             and all(isinstance(v, int) for v in values)\
             and len(values) == 2:
            for i in range(values[0], values[1]):
                self.tab.append(float(i))
            self.size = len(self.tab)
        else:
            print("Error: Vector can't be initialized.")
            exit(1)

    def verify(self, vec, operation):
        if type(vec) is not Vector:
            if operation in("+", "-"):
                print("Error: Variable is not a vector.")
                exit(1)
            if operation in("/", "*"):
                if type(vec) not in(int, float):
                    print("Error: Variable is not scalar(int or float).")
                    exit(1)
                if type(vec) in(int, float)\
                   and vec == 0:
                    print("Error: Division by 0.")
                    exit(1)
        if type(vec) is Vector:
            if operation == "/":
                for v in vec.tab:
                    if v == 0:
                        print("Error: Division by 0.")
                        exit(1)
            if vec.size != self.size:
                print("Error: Vectors must be the same size.")
                exit(1)

    def __add__(self, to_add):
        self.verify(to_add, "+")
        result = []
        for i in range(0, self.size):
            result.append(self.tab[i] + to_add.tab[i])
        return Vector(result)

    def __radd__(self, to_add):
        return self + to_add

    def __sub__(self, to_sub):
        self.verify(to_sub, "-")
        result = []
        for i in range(0, self.size):
            result.append(self.tab[i] - to_sub.tab[i])
        return Vector(result)

    def __rsub__(self, to_sub):
        self.verify(to_sub, "-")
        result = []
        for i in range(0, self.size):
            result.append(-to_sub.tab[i] + self.tab[i])
        return Vector(result)

    def __truediv__(self, to_div):
        self.verify(to_div, "/")
        result = []
        if type(to_div) is Vector:
            for i in range(0, self.size):
                result.append(self.tab[i] / to_div.tab[i])
        elif type(to_div) in(int, float):
            for i in range(0, self.size):
                result.append(self.tab[i] / to_div)
        return Vector(result)

    def __rtruediv__(self, to_div):
        print("Error: Variable is not a vector.")
        exit(1)

    def __mul__(self, to_mul):
        self.verify(to_mul, "*")
        result = []
        if type(to_mul) is Vector:
            for i in range(0, self.size):
                result.append(self.tab[i] * to_mul.tab[i])
        elif type(to_mul) in(int, float):
            for i in range(0, self.size):
                result.append(self.tab[i] * to_mul)
        return Vector(result)

    def __rmul__(self, to_mul):
        self.verify(to_mul, "*")
        result = []
        if type(to_mul) is Vector:
            for i in range(0, self.size):
                result.append(self.tab[i] * to_mul.tab[i])
        elif type(to_mul) in(int, float):
            for i in range(0, self.size):
                result.append(self.tab[i] * to_mul)
        return Vector(result)

    def __str__(self):
        txt = str(self.size)
        txt += str(self.tab)
        return txt

    def __repr__(self):
        return repr(self.tab)
