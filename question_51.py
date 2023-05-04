

class American():
    @staticmethod
    def printNationality():
        print("American")

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
aNewYorker.printNationality()