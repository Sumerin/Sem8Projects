import math

class Calculator():

    def __init__(self):
        self.Display = "0"
        self.__decimalSign = False
        self.__countRegister = 0
        self.__swapNumber = True
        self.__lastSign = "="
        self.__earseMinus = True
        self.__memoryRegister = 0
        self.IsNegative = False
        self.IsMemorized = False
        self.Error = False
        self.__restorePressed = False
        self.__clearPressed = False

    def Press(self, char):

        if self.Error and char != "C/CE":
            return None
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
            "C/CE": self.clear,
            "M+": self.memorize,
            "M-": self.memorize,
            "MRC": self.restore,
            "sqrt": self.sqrt,
            "p": self.percent
        }
        func = switcher.get(char)
        func(char)

    def typeNumber(self, char):
        if len(self.Display) > 10 and self.__swapNumber is False:
            return None
        self.__clearPressed = False
        self.__restorePressed = False
        if char == '0' and len(self.Display) == 1 and self.Display[0] == '0':
            pass
        elif self.__swapNumber:
            if self.__earseMinus:
                self.IsNegative = False
            self.Display = char
            self.__swapNumber = False
            self.__earseMinus = False
        else:
            self.Display += char

    def decimalChar(self, char):
        self.__clearPressed = False
        self.__restorePressed = False
        if self.__decimalSign is False:
            if self.__swapNumber:
                self.Display = "0"
            self.Display += char
            self.__decimalSign = True
            self.__swapNumber = False

    def typeSign(self, char):
        if self.__earseMinus is True and char == '-':
            self.IsNegative = True
            self.__earseMinus = False
            return None

        try:
            self.proceed(self.__lastSign)
            self.registerToDisplay(self.__countRegister)
            self.__lastSign = char

        except:
            self.Display = "0"
            self.Error = True

        if char == '=':
            self.__countRegister = 0

        self.__swapNumber = True
        self.__decimalSign = False
        self.__clearPressed = False
        self.__restorePressed = False

    def proceed(self, char):
        value = float(self.Display)
        if self.IsNegative:
            value *= -1
        self.__earseMinus = True

        if char == "=":
            self.__countRegister = value
        elif self.__swapNumber and self.__restorePressed is False:
            return None
        elif char == '+':
            self.__countRegister += value
        elif char == '-':
            self.__countRegister -= value
        elif char == 'x':
            self.__countRegister *= value
        elif char == '/':
            self.__countRegister /= value

    def registerToDisplay(self, value):
        if value < 0:
            value *= -1
            self.IsNegative = True
        else:
            self.IsNegative = False

        if value % 1 != 0:
            self.Display = str(value)
        else:
            self.Display = str(int(value))

        if len(self.Display) > 11:
            self.Error = True
            #self.Display = "0"

    def clear(self, char):
        self.__restorePressed = False
        if self.__clearPressed is False:
            self.__clearPressed = True
        else:
            self.__memoryRegister = 0
            self.IsMemorized = False
        self.Display = "0"
        self.__decimalSign = False
        self.__swapNumber = True
        self.IsNegative = False
        self.__earseMinus = True
        self.__restorePressed = False
        self.Error = False

    def memorize(self, char):
        self.__restorePressed = False
        self.IsMemorized = True
        value = float(self.Display)

        if self.IsNegative:
            value *= -1

        if char[1] == "+":
            self.__memoryRegister += value
        else:
            self.__memoryRegister -= value

        self.__swapNumber = True
        self.__decimalSign = False
        self.__earseMinus = True

    def restore(self, char):
        self.__clearPressed = False
        self.registerToDisplay(self.__memoryRegister)
        if self.__restorePressed is False:
            self.__restorePressed = True
        else:
            self.__memoryRegister = 0
            self.IsMemorized = False

    def sqrt(self,char):
        self.__clearPressed = False
        self.__restorePressed = False
        value = float(self.Display)
        if self.IsNegative:
            self.IsNegative = False
            self.Display = "0"
            self.Error = True
            return None
        self.registerToDisplay(math.sqrt(value))

    def percent(self, char):
        self.__clearPressed = False
        self.__restorePressed = False
        if self.__lastSign == '=':
            return None
        elif self.__lastSign == "/" or self.__lastSign == "x":
            self.Display = str(float(self.Display) / 100)
            self.typeSign(char)
        elif self.__lastSign == "+" or self.__lastSign == "-":
            self.Display = str(self.__countRegister * (float(self.Display) / 100))
            self.typeSign(char)