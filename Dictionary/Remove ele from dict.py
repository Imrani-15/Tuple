# creating a  nested Dictionary
Dict = {'School' : 'Vikas', 'college': 'Sriharsha', 'pg': 'k.c.p.g', 'Grades': {10: 6.0, 12: 6.1, 'pg': 7.9}}
print("\nInitial Dictionary:")
print(Dict)

# delecting a key value
del Dict['college']
print("\nDelecting a key value:")
print(Dict)

# Delecting a nested a key value from the Dictionary

del Dict['Grades'][12]
print("\nDelecting a nested a key value from the Dictionary:")
print(Dict)

# Using clear() Method
print("\nDeleting a items in the Dictionay:")
Dict.clear()
print(Dict)

# Adding  element to a Dictionay
Dict['one'] = 'apple'
Dict['two'] = 'oranges'
Dict['three'] = 'grapes'
print("\nAdding element to a Dictionary:")
print(Dict)

# Using pop() method
pop_ele = Dict.pop('one')
print("\nRemove the one item from dict by using pop() method:")
print(Dict)
print(pop_ele)

# using popitem() method
pop_ele1 = Dict.popitem()
print("\nRemove the one item from dict by using popitem() method:")
print("\nprint the pair returned:")
print(pop_ele1)
print("\nprint the dict after operation")
print(Dict)