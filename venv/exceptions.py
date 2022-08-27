"""
Errors terminates the python code been executed
    - Syntax error
        - shows the error with ^
        - most IDE catches this error
    - exceptions: errors that occur during execution
        - code is syntactically correct
        - but error occurs when you try to execute it

exception handling:
Try: block of code that might generate error / run this code
except: handle the exception
else: execute code when there is no error
finally: executes whether an error occurs or not

"""

try:
    print(10/2)
except:
    print("print nothing")
else:
    print("No error")
finally:
    print("I occur regardless of an error")

try:
    x = 10
    y = [10, 2, 3, 0, 4, 6]
    z = [x/m for m in y]

except:
    print("error")
finally:
    print("I occur regardless of an error")


"""
Example: database connection
try: make a connection 
except: error
finally: close the connection

read and write to a file 
try: read the file
    write to a file
except: error that occurs
finally/else: close the fail
"""

"""
types of Exceptions
- Arithmetic error : Zerodivision Error  eg10/0
                     OverflowError 
- Assertion error: when assertion fails
- EOF error 
- Import error
- ModuleNotFound error
- Index error
- Key error
- Name error
"""

try:
    print(name)
except NameError as err: #named exceptions
    msg = err
    print(f"A new message: {err}")
except:
    print("other errors")


"""Creating customized Exceptions"""
class NoNegativeInList(Exception):
    pass

"""raise exceptions"""

list1 = [10, 4, 5, 6, -1, 7, 7]

for x in list1:
    if x < 0:
        raise NoNegativeInList("Negative values shouldn't be in a list")