
class Calculator():

    def __init__(self):
        self.Display = "0"
        self.__decimalSign = False
        self.__countRegister = 0
        self.__swapNumber = True
        self.__lastSign = "="
        self.IsNegative = False

    def Press(self, char):
        switcher = {
            "0": self.typeNumber,
            "1": self.typeNumber,
            "2": self.typeNumber,
            "3": self.typeNumber,
            "4": self.typeNumber,
            "5": self.typeNumber,
            "6": self.typeNumber,
            "7": self.typeNumber,
            "8": self.typeNumber,
            "9": self.typeNumber,
            ".": self.decimalChar,
            "+": self.typeSign,
            "-": self.typeSign,
            "=": self.typeSign,
            "x": self.typeSign,
            "/": self.typeSign,
        }
        func = switcher.get(char)
        func(char)

    def typeNumber(self, char):
        if char == '0' and len(self.Display) == 1 and self.Display[0] == '0':
            pass
        elif self.__swapNumber:
            if len(self.Display) != 1 or self.Display[0] != '0':
                self.IsNegative = False
            self.Display = char
            self.__swapNumber = False
        else:
            self.Display += char

    def decimalChar(self, char):
        if self.__decimalSign is False:
            if self.__swapNumber:
                self.Display = "0"
            self.Display += char
            self.__decimalSign = True
            self.__swapNumber = False

    def typeSign(self, char):
        if self.__swapNumber and char == '-':
            self.IsNegative = True
            return None

        self.proceed(self.__lastSign)
        self.registerToDisplay()
        self.__lastSign = char

        if char == '=':
            self.__countRegister = 0

        self.__swapNumber = True
        self.__decimalSign = False

    def proceed(self, char):
        value = float(self.Display)
        if self.IsNegative:
            value *= -1
        self.IsNegative = False

        if char == "=":
            self.__countRegister = value
        elif self.__swapNumber:
            return None
        elif char == '+':
            self.__countRegister += value
        elif char == '-':
            self.__countRegister -= value
        elif char == 'x':
            self.__countRegister *= value
        elif char == '/':
            self.__countRegister /= value


    def registerToDisplay(self):
        value = self.__countRegister
        if value < 0:
            value *= -1
            self.IsNegative = True
        else:
            self.IsNegative = False

        if value % 1 != 0:
            self.Display = str(value)
        else:
            self.Display = str(int(value))
