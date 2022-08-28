from typing import List, Optional, Union

"""
Clean code rules:
-Correct function names that describes what the function noes
- documentation
-Type annotation: type hitting ( -> )
    Union = a or b or c
    Optional = a or None
- single responsibility of functions and classes

PEP8 = 4 space, blank lines  https://peps.python.org/pep-0008/
"""

def convert_to_celcius(farheit: Union[float, int]) -> float: # -> to 4to budet pokaz6vat/vozvrawat
    return (farheit - 32) * 5/9



def welcome_to_class(name: str) -> None:
    print("Welcome")

class Calculator:
    """
    A class that simulates the scientific calc

    :parameter
    number - am integer that you want to perform action on. default value = 0

    :method
    - add

    """
    def __init__(self, number:float = 0) -> None:
        self.number = number
        self.rst = 0

    def add(self, num = 0):
        self.rst += num


    # TODO: add method multiply and subtract

class AWSConnection:
    pass

cal = Calculator


def get_active_account(user_id:str = None) -> List:
    acct = []
    if user_id == None:
        return acct # return list of all active accs
    acct.append(user_id)
    return [user_id] # returns only 1 user acct

def get_accout_info(user_id):
    pass