f"""
Objects oriented programming

objects has properties and methods.
    An object is a instance of a class

Class is a blueprint for creating objects

Advantages of OOP
    - help you bundle functionalities together
    - easy creation of a class instance object
    - ability to modify methods of a class without changing the class
    - create user-defined data structure



car: class
    - minimum size - max size
    - 4 tyres / wheels
    - windows and windshields
    - headlamps
    - max min seating
    - stearing wheel

objects: Hyundai, Subaru, Toyota, MB, Tesla, Volvo

Students: class
    - Course
    - Location
    - Method  = remote/physical

objects: DS est 1, DS est 2, DS PH, Python


class <<Class_name>> class name should start with Capital letter
    pass 

class has methods - functions defined in the body of the class. 
    First argument in the function is self
    has attributes - variables defined in a class 
    
1) __init__  - constructor

- num of doors
- maximum speed 
- max passengers 
- name 

2) def <<method_name>>(self, <<any_parameter>>)
"""

class Car:
    def __init__(self, name, num_doors=4, exotic = False):
        self.name = name #says, that is it class attribute
        self.door_no = num_doors
        self.is_exotic = exotic
        self.in_motion = False
        self.speed = 0

    def get_doors(self):
        if self.door_no not in [2,3,4]:
            return f"{self.name} has invalid door nrs"
        return self.door_no

    def drive(self):
        self.in_motion = True


    def acceleration(self, acceleration= 10):
        if self.in_motion:
            self.speed += acceleration

    def stop(self):
        self.in_motion = False



car1 = Car(name = "Toyota Prius", num_doors= 4)
car2 = Car(name = "Tesla", num_doors= 2, exotic= True)
print(car1)
car2.drive()
car2.acceleration(30)
print(car1.speed)
print(car2.speed)
