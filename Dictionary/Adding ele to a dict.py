# Adding element to dictionary in python

Dict = {}
print("\nEmpty Dictionary:")
print(Dict)

# adding element one at a time
Dict[1] = 'oneapple'
Dict[2] = 'twoapple'
Dict[3] = 'threeapple'
print("\nAdding three element to dictionary:")
print(Dict)

# Adding set of values to a single key
Dict['marks'] = [20,50,60,35]
print("\nAdding a set of values to a single key:")
print(Dict)

# Updating exiting key's value
Dict[2] = 'two Oranges'
print("\nupdating exiting key's value:")
print(Dict)

# Adding nested key value to dictionary
Dict[5] = {'city': 'Tenali', 'state details': {'state': 'Andhra Pradesh', 'Pincode': 522202}}
print("\nAdding nested key value to dictionary:")
print(Dict)

#Accessing elements from a Dictionary
Dict1 = {'name': 'Imrani', 'RollNo': 105, 'city': 'Tenali'}
print("\nAccessing elements from a Dictionary:")
print(Dict1['name'])

# Accessing a element using get() method
print("\nAccessing a element using get() method:")
print(Dict1.get('RollNo'))

# Creating a nested dictionary
Dict2 = {'one': {'apple': 2}, 'two': {'oranges': 5}}
print("\nCreating a nested Dictionary:")
print(Dict2)

# Accessing elements from a Dictionary
print("\nAccessing elemets from a Dictionary:")
print(Dict2['one'])
print(Dict2['two']['oranges'])