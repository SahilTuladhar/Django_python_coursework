value = input("Enter a value: ")

value = int(value)

if (type(value) == str):
    print(value , 'is a string')
elif (type(value) == int):
    print(value , 'is an integer')
else:
    print(value ,'ist a float')

