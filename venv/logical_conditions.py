"""
logical cons evaluates to boolean (True,False)
a == b {equals}
a != b {not equals}
a < b

"""

if 10 < 5:
    print("less than 5")
else:
    print("not less than 5")
"""
T and T = T
T and F = F
F and T = F
F and F = F
"""
marks = [90, 75, 80, 60, 72]
grade = []
for mark in marks:
    if mark >= 90:
        grade.append('A+')
    elif mark >= 80 and mark <90:
        grade.append('A')
    elif mark >= 70 and mark <80:
        grade.append('B')
    elif mark >= 60 and mark <70:
        grade.append('C')
    else:
        grade.append('Fail')
print(grade)