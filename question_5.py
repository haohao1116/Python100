class Method(object):
    def __init__(self):
        self.s =''
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

if __name__ == '__main__':
    m = Method()
    m.getString()
    m.printString()

