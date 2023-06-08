## MAPPING KEYS TO MULTIPLE VALUES IN DICTIONARIES

dict1 = {
    'suyan' : [1,2,3,4,5],
    'shristi' : ['a','b','c']
}   
print(dict1)
#also can be implemented as set in values section instead of list
#use list to preserve the insertion order of items
#use set to eliminate duplicates and dont care bout order

#using defaultdict 
from collections import defaultdict

dict2 = defaultdict(list)
for i in range(5): 
    dict2['suyan'].append(i)
    dict2['shristi'].append(i+2)
print(dict2)

dict3 = defaultdict(set)
for i in range(3): 
    dict3['suyan'].add(i)
    dict3['shristi'].add(i+2)
print(dict3)


## KEEPING DICTS IN ORDER
# orders the items on the basis of their insertion
from collections import OrderedDict
d4 = OrderedDict()
d4['suyan'] = 4
d4['shristi'] = 3
d4['ajax'] = 5
d4['techtim'] = 2
d4['apple'] = 1
d4['wow'] = 0

for key in d4:              #for key,value in d4: print(key,value)
    print(key,d4[key]) 
# OrderedDict internally maintains a doubly linked list, and is twice as large as normal dictionary


## CALCULATING WITH DICTS
percent = {
    'suyan' : 75.67,
    'Shristi' : 84.88,
    'Ajax' : 45.45,
    'Ram' : 65.68
}

min_percent = min(zip(percent.values(), percent.keys()))
print(min_percent)

max_percent = max(zip(percent.values(), percent.keys()))
print(max_percent)

sorted_percent = sorted(zip(percent.values(), percent.keys()))
print(sorted_percent)

# use zip function to combine keys and values into pairs, creating an iterable of tuples


## FINDING COMMONALITIES BETWEEN TWO DICTIONARIES

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'suyan' : 1,
    'shristi' : 2,
    'z' : 3
}

a.keys() & b.keys()
b.keys() - a.keys()
a.items() & b.items()