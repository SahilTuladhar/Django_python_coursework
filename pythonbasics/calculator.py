def calc(num1 , num2 , op):

 if op  == '+': 
    print(num1+num2)
 elif op == '-':
   print(num1 - num2)
 elif op == '*':
   print(num1 * num2)
 elif op == '/':
   print(num1 / num2)
 else:
   print('invalid operatpor. Please enter right operator')


num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
op = input('Enter operator:')

calc(num1,num2 , op)

