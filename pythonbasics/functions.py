def greetings(names):
    print("Hi there," , names[1])


name_list = ['Messi' , 'Suarez' , 'Neymar']

greetings(name_list)

def greetings1(*names):
    print("Hi there," , names[1])

greetings1("Suarez" , "Messi" , " Neymar")

def sum(num1 , num2): 
    return num1 + num2 

addition = sum(10 , 5)

print(addition)