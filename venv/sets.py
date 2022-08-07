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
print(len(myset))  # len kollvo/dlina

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

citrus = ['oranges', 'tangerine', 'lemon', 'lime']  # [] = list
myset.update(citrus)
print(myset)

"""
Removing elements from set:
    - remove <<set>>.remove(<<item>>) generates error if item doesnt exists
    - pop: removes last item in the set. But remember that a set is unorder, so you dont know what it removes
    - discard : doesnt return error if no item
    - clear
"""
myset.remove('guavas')
print(myset)
myset.pop()
print(myset)


"""
Joining of set:
    - union: create a new set with item from 2 sets.
Union also remove duplicates if it occurs


"""

set1 = {'cantaloupe', 'berries', 'mangoes', 'lime', 'tangerine'}
set2 = {'oranges', 'almonds', 'cashews', 'peanut', 'honeydew', 'lemon'}

set3 = set1.union(set2)
print(set3)

"""
To get common values(duplicates) within a set
 - intersection <<set1>>.intersection(<<set2>>)
 - intersection_update = what is common to both
"""

set1.intersection_update(set2)
print(set1)

print(set3)
print(set2)
set3.symmetric_difference_update(set2)
print(set3)

print(set3.isdisjoint(set2))
