"""
Inheritance:
    - inheriting attributes and methods from base/ parent class
    - derived/child class can have it's own attributes and methods

class <<ChildClassName>>(BaseClass):
    def __init__(self):
        super().__init__()

class <<ChildClassName>>(BaseClass):
    def __init__(self):
        BaseClass().__init__()
"""

"""
class rectangle:
attributes - length and breadth
methods - perimeter, area

child class = Paralleligram
    - inherits from rectangle
    - attributes = heights
    - volume
"""

class Rectangle:
    def __init__(self, len = 5, brd = 6):
        self.length = len
        self.breadth = brd

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.breadth * self.length

    def show(self):
        print(f" Rectangle Info: \n"
              f"length: {self.length} \n"
              f"breadth: {self.breadth} \n"
              f" Area: {self.area()} \n"
              f" Perimeter: {self.perimeter()}")

class Parallelogram(Rectangle):
    def __init__(self, len, brd, height):
        super().__init__(len, brd)
        self.height = height

    def volume(self):
        return self.length * self.breadth * self.height

    def show(self):
         print(f" Parallelogram Info: \n"
              f"length: {self.length} \n"
              f"breadth: {self.breadth} \n"
              f" Area: {self.area()} \n"
              f" Perimeter: {self.perimeter()} \n"
               f"Volume: {self.volume()}")
# mozno na show1 pomenjat i ne psiat vsjo
# def show1(slef)
    # self.show()
# i dobavit tolko volume f"Volume: {self.volume()}"

rect1 = Rectangle()
rect1.show()

para1 = Parallelogram(6,7,4)
para1.show()
