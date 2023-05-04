import math


class Rectangle():
  def __init__(self,length,width):
      self.length = length
      self.width = width

  def computer_area(self):
       return self.width  * self.length



c = Rectangle(5,4)
print(c.computer_area())
