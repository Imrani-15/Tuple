# Creating Tuple
# empty tuple
Tuple = ()
print("\nInitial empty Tuple:")
print(Tuple)

# Creating a tuple with the use of string
tuple1 = ("dog","cat","papy")
print("\ntuple with the use of string:")
print(tuple1)

# Creating a tuple with the use of list

list = [20,12,32,25,41]
print("\ntuple with the use of list:")
print(tuple(list))

# Creating a tuple with the use of built in function
tuple2 = tuple('grapes')
print("\ntuple with the use of built in function:")
print(tuple2)

# Creating a tuple with mixed datatype
T = (5,'herbal',7.0,'nutrition')
print("\ntuple with mixed datatype:")
print(T)

# Creating a tuple with nested tuples
T1 = (1,23,4,5)
T2 = ('dairy milk','5star','Milkbar')
T3 = (T1,T2)
print("tuple with nested tuples:")
print(T3)

# Creating a tuple with repetition
repe = ('ink',) * 2
print("\ntuple with repetition:")
print(repe)

# creating a tuple with the use of loop
num = ('imrani')
n = 6
for i in range(int(n)):
    num = (num,)
    print(num)