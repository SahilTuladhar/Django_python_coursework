from math import * # some built in functions  needs to be imported from the math library eg . sqrt

numbers = [ 1 , 2, 3, 5, 12]
num = 21
num1 = str(num)
even_numbers = []

print(max(numbers))

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)


print(even_numbers)

print(type(num1))

print(round(12.326 , 2))

print(sqrt(16))