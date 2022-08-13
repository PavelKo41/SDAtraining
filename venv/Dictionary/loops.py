"""
while loop:
executes a set of sentence until the condition is no longer valid
"""
i = 10

while i > 3:
    print(i)
    i -= 2 #i = i -1


"""
break:
stops you loop even if the condition is valid
"""

i = 10

while i > 3:
    print(i)
    if i == 6:
        break
    i -= 2 #i = i -1

for x in range(i):
    print(x)
    if x == 6:
        break

"""
continue: stop the current iteration  and advance to the next
"""

i = 10

for x in range(i):
    if x == 6:
        continue
    print(x)


"""
"""
name = input("What is your name")
print(f"My name is {name}")