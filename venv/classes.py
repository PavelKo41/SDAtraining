"""
class method:
    - called on the class itself, not on an object instance
    - can only access you class variables
    - takes the first argument as a class (cls)

    <<class>>.<<class_method>>

"""

"""
static method:
    - general utility methods that perform tasks in isolation
    - dont take self on cls parameters
    - bound to class but not the object of the class
    
    
Access restrictions:
    - Private = only accessible within the class  # dobavlaja __ delaet private
    - Public = accessible everywhere (class,object, inheritance)
    
    
"""

class Student:
    study_type = "remote"
    def __init__(self, name, age, cohort):
        self.name = name
        self.age = age
        self.cohort = cohort

    def print_std(self):
        print(f"name: {self.name}\n age: {self.age} \n study type: {self.study_type} \n cohort: {self.cohort}")

    def __myprivate_var(self):
        print("I am private")


    @classmethod #decorator
    def set_study_type(cls, mode):
        cls.study_type = mode

    @staticmethod
    def is_weekend(day):
       return day in [5,6]

    @staticmethod
    def sample_std():
        print(f"name: sample \n age: 10 \n study type: MODE")


std1 = Student("name", 28, "DS1")
std1.print_std()

Student.set_study_type("Hybrid")

std1.print_std()
Student.sample_std() # eto i sled odno i toze vqzqvajet
std1.sample_std()
