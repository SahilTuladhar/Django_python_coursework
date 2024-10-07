
file = open("C:/Users/Sahil/Desktop/Django/pythonbasics/file.txt" , 'r')

print(file.readable())

# print(type(newfile.readlines()))

# print(newfile.readlines())

for lines in file.readlines():
    print(lines)

file.close()

with open("C:/Users/Sahil/Desktop/Django/pythonbasics/newfile.py" , 'w') as  newfile:

 newfile.write("print('this is the new line')")

newfile.close()
