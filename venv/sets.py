"""
Set:
 - a collection
 - unordered (vsegda v razbros kidaet)
 - unchangeable
 - unindexed, you cannot access then throught index
 - created/denoted with {}
 - set do not allow duplicates

"""

myset = {'mangoes', 'guavas', 'berries', 'honeydew', 'mangoes'}
print(myset)
print(len(myset)) # len kollvo/dlina

for x in myset:
    print(x)

print('honeydew' in myset)

"""
Add items to a set:
    - add <<set>>.add(<<item>>)
    - update - adds items from a set into another sets
            <<set1>>.update(<<set2>>)
    - add any collection to a set
    
"""

myset.add('cantaloupe')
print(myset)

nuts = {'cashews', 'peanut', 'almonds', 'guavas'}
myset.update(nuts)
print(myset)

citrus = ['oragnes', 'tangerine', 'lemon', 'lime']  # [] = list
myset.update(citrus)
print(myset)
