"""
Zip:
Easily combine 2 lists

In order to see the content of a zip, it must be casted to a list

if different lengths, the result will be the shorted list


"""

name = ["Oyin", "Thomas", "Frank", "Imma", "Corey"]
surname = ['komolafe', 'udoh', 'White', 'Mcneil']
age = [28, 30, 20, 18]

print(list(zip(name, surname, age)))
