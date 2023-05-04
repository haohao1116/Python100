import math


class Circle():
  def __init__(self,r):
      self.r = r

  def computer_area(self):
        print(math.pi * self.r *self.r )



c = Circle(5)
c.computer_area()
