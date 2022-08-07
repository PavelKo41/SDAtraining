"""
    list are used to store multiple values in a variable
    list are denoted/created using
    list are ordered collection of items
    allow duplicates
    changeable - add, remove, replace
"""
mylist = ['apples', 'mangoes', 2 , 7, 5, 'red' ]
print(type(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[2:4])

# use in to check if a value exists in a list
print('guava' in mylist)

"""
    Add items to list
    - append: add to the end of list
    - insert: add at specific index
            <<list>>.insert(<<position>>, value)
    -extend: appends elements from a list to another list (end)
                    <<current_list>>.extend<<new_list>>
"""
mylist.append('guavas')
mylist.append('grapes')
mylist.insert(2, 'blueberries')
mylist.insert(0, 'melon')
print(mylist)

exotic_fruits = ['cashew', 'blueberries', 'passion']

mylist.extend(exotic_fruits)
print(mylist)

mylist[4] = "corn"
print(mylist)

"""
remove items:
    - remove: <<list>>.remove(<<item>>)
        - with duplicate, the first removes
    - pop: removes the last item <<list>>.pop()
     <<list>>.pop(<<index>>): removes item at the position
    - clear: removes all the items in a list
"""
mylist.remove(7)
mylist.remove(5)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
exotic_fruits.clear()
print(exotic_fruits)

age = [12, 14, 25, 39, 67, 45, 13]
print(min(age))
print(max(age))
print(sum(age))
print(sum(age) / len(age))

mylist.sort() #sortiruet po alfavitu
age.sort()
print(mylist)
print(age)

mylist.reverse()
print(mylist)

"""
Looping throught list
    - for loop
        for <<variable>> in <<list>>:
            statements
    - range: allows you to watch throught index      
"""
name = "Pavel"
ages = 29

#print(f"My name is {name}, I am {ages} years old")
#print("My name is"+ name + "I am" + str(ages)+ "years old")
#print("My name is {} and I am {} years old".format(name,ages))

for var in mylist:
        print(f"I love {var}") # f string
        #print("I love "+ var)  # 2 i 3 odno i toze
        #print("I love {}".format(var))


for item in age:
    print(item/2)

"""
range(start, stop, step)
default step is 1
"""

for i in range(len(age)):
    print(f"index {i}: {age[i]}")

"""
List Comprehension:
    - creates a new list
    - short method to creating a list from an existing list
    - filter and perform operations
     
     [<<expression>> for <<variable_name>> in <<list>> <<optional: condition>>]
"""
[print(f"My Age is {x} ") for x in age]

new_age = [x + 10 for x in age if x%2 == 0]

print(new_age)

upp_list = [var.upper() for var in mylist]

print(upp_list)
