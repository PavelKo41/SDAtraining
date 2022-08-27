"""
python
    - create a function inside another function
    - pass a function as an argument to another function

A decorator is a function that takes another function and extends the behaviour of the latter function without explicity
modifying it

"""

def increment_num(num):
    return num + 2

print(increment_num(3))

"""
Using a function as argument
"""

def welcome_sudent(name):
    return (f"Welcome {name} from the break")

def did_you_study(name):
    return f" I hope you studied and revised python {name}"

def greetings(any_func):
    return any_func("Pavel")

print(greetings(did_you_study))
print(greetings(welcome_sudent))

"""
create function inside another  function  - nested
    - inner functions are not defined until the parent function is called/executed
    - inner function is local to your function, hence they are not available outside the parent
"""

def outer_box(): #parent function
    print("This is the parent box")

    def middle_box(): #inner function
        print("This is the middle box")

    def last_box(): #inner function
        print("This is the last box" .upper())

    middle_box()
    last_box()

outer_box()

"""
function returning another function

"""


def greeting(hour):
    def morning(name):
        return f"Good morning {name}"

    def afternoon(name):
        return f"Good afternoon {name}"

    def evening(name):
        return f"Good evening {name}"

    def night(name):
        return f"Good night {name}"

    if hour < 12: #0-11
        return morning
    elif hour >= 12 and hour <= 17:
        return afternoon
    elif hour >= 17 and hour < 20:
        return evening
    else:
        return night

greet = greeting(14)
print(greet("Pavel"))


"""
decorator
    - takes a function as an argument
    - defines an inner function
    - returns the function as the result of its operation
"""

def my_decorator(func):

    def wrapper():
        print(f"This is my wrapper")
        func()
    return wrapper

def say_cheese():
    print("Python is fun!")

#say_cheese()
my_decorator(say_cheese)() #tut skobki nado tak togda piwet moi wrapper

@my_decorator
def say_something():
    print("Saying something")

say_something()


def increment(func):
    def wrapper(*args, **kwargs):
        num = sum([x**2 for x in args])
        num2 = sum([x+2 for x in args])
        return func(num, num2)
    return wrapper

@increment #esli stavit @ to budet dekorirovat, no predvoritelno nado sozdat dekorator
def just_a_num(num):
    return num + 3

@increment
def two_nums(num1, num2):
    return num1+3, num2+3


#print(just_a_num(5))
print(two_nums(10,8))

"""
a,b,c = (10,3,6)  *args  == positional arguments

**kwargs == named arguments
num1 = 3, num2 = 10, num3 = 6

positional comes before named
"""

