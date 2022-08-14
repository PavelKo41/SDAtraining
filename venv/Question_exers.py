"""
Q1 2 strings, can you make 1 string from second by deleting characters
"""
s1 = "Hello"
s2 = "vufigsaHudesdflelio"

count = 0
for ch in s1.lower():
    if ch in s2.lower():
        count += 1

print(count)

if count == len(s1):
    print("Possible")
else:
    print("Impossible")



"""
Q2 sum numbers until flag -9999 is seen
"""

list1 = [10, 23.4, 67, -9999, 7, 8, 100]

def sum_number(nums:list1) -> float:
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x
        else:
            break
        return sum
    sum_number(list1)

"""
Q3 find min and max in set
"""
set = {10, 15, 22, 5, 9, 120}
print(min(set))
print(max(set))

"""
Q4 count the number of odd and even 
"""
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

