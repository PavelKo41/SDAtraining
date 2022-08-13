"""
A function is a block of code/sentences that runs only when it is called
    - can have parameters, i.e it can accept input
    - it can return a result



def <<function_name>>() without parameters and not return values/results
    sentences
def<<gunction_name>>() without parameters and heer returns values/results
    sentences
    return<<data>>
"""

def print_name():
    name = input("Your name")
    print(f"What a nice name {name}!!")

# call a function by its name
print_name()

def return_name():
    name = input("Your name")
    return name
fname = return_name()
print(f"You have a lovely name {fname}")

"""
def <<function_name>>(<<argument>>,.......,<<arguments>>):
    sentences   
    return<<data>>
"""
def my_name(name, age):
    print(f"You have a lovely name {name} for you age {age}")

my_name("Pavel" , 29)
my_name(29, "Pavel")
my_name(age = 29, name="Pavel") #named argument

#calling your function
# func_name(<<name_param>> = value)

def area_of_a_square(length):
    return length **2
def area_of_rectangle(len, breadth):
    return len * breadth

def get_shape(len, breadth):
    if len == breadth:
        area = area_of_a_square(length=len)
        print(f"Shape is a square with area {area}")
    else:
        print(f"Shape is a rectangle with area {area_of_rectangle(len,breadth)}")

get_shape(len=10, breadth=10)
# get_shape (10, 10) odno i toze
