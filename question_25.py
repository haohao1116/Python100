class Param():
    s = 0

    def __init__(self,s = None):
        self.s = s

p = Param(1)
print(p.s)
print(Param.s)