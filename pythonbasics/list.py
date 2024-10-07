# Method 1 : using []
names = ["Ram" , "Hari" , " shyam" , 'Sita']

print(names[1:3])

print(names[1:])

print(names[:3])

print(names[-1])

print(names.pop(0))

# Method 2: using list constructor

numbers = list((1 , 2, 3, 4 , 5))

print(numbers)

print(numbers.index(4))


# List can contain items of different data types

li = ["Hari" , 18 , True]

print(type(li))

print(type(li[0]))

print(type(li[1]))

print(type(li[2]))