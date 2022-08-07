"""
 - strings in python are arrays
 - the first position is 0 for array_like objects
"""

hello = "Welcome to python"
#print(hello[0]) #  pervuju bukvu vqvedet na ekran (W)

"""
 looping throught string = 
    - for <<variable_name_for_each_char>> in  <<string>>:
    
"""
for cr in hello:
    print(cr)

"""
    length of a string: len()
"""
print(len(hello))

"""
    Check if character or phrase exists: in

"""
txt = "it's a beautiful day"
print("beau" in txt)
print("day" not in txt)

"""
    slicing of strings <<string>>[<<start_index>>:<<end_index>>]
    slice from a position to end: <<string>>[<<start_index>>:]
    slice form end to a position: use negative index
"""

print(txt[3:7])
print(txt[7:])
print(txt[-1]) # returns the last character in array
print(txt[-4:-1])

"""
lower() or casefold() = return to lowercase
https://docs.python.org/3/library/stdtypes.html
"""
print(txt.capitalize()) #returns 1 character as capital letter(zaglavnaja)
print(txt.upper()) # vsjo zaglavnqmi
print(txt.count('t')) # skolko raz bukva
print(txt.endswith('x')) # returns true if strings ends with a specified value
print(txt.find('ful'))
