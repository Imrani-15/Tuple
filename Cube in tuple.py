# Python program to create a list of tuples from given list having number and its cube in each tuple
List = [1,2,3,4]
cube = [(val,pow(val,3)) for val in List]
print(cube)