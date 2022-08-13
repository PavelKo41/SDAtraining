"""
key: value pair
ordered in pyhton 3.7 - and others
it is changeable
keys do not allow duplicate

{
<<key>>: <<value>>,
<<key>>: <<value>>
}

"""

std = {
    "name" : "Pavel",
    "age" : 29,
    "occupation" : "Police officer"
}

"""
Acess items in a dict: 
    - using keys as index
    - use get method
        <<dict_name>>.get(<<key_to_get>>)
"""
print(std["age"])
print(std.get("ages"))


"""
Get all keys
    - keys method returns a list of all the keys in a dict
    <<dict>>.keys()
"""
print(std.keys())

"""
Add items to a dict:
    -use key_value pair
        <<dict>>[<<new_key>>] = <<value>>
    -update()
    <<dict>>.update({
                    <<key>>:<<value>>
                    )}
"""

std["is_student"] = "No"


std.update({
    "best_color": "black"
})
print(std)

"""
Remove items in a dic: 
    - pop
    <<dictionary>>.pop(<<key>>)
    
    - popitem() remove last item in dict
    - clear() : empties a dic
"""
std.pop("is_student")
print(std)


"""
Loop through dict:

    - values() : returns the value in the dict

"""

for item in std: #returns the key or use <dict>.keys()
    print(item, std[item])

for val in std.values(): # returns dict values
    print(val)

for key, val in std.items(): #returns keys and values
    print(f"{key}:{val}")

print({k: str(v).upper() for k,v in std.items()}) #mozno menjat v i k : k i v

"""
Nested dicts
<<dict>> = { 
<<key>>: {
          <<key>>:<<value>>
          ....
          <<key>>:<<value>>
          
    }
}
"""

students = {
    "Pavel": {
        "is_std": False,
        "age": 28
     },
    "Thomas": {
        "is_std": True,
        "age": 20
    },
    "Frank": {
        "is_std": True,
        "age": 30,
        "hair_color": "red"
    }
}
print(students.keys())

