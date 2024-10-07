try:
    num = int(input("Enter a number:"))

    if num % 2 == 0:
       print(num)
    else:
        print(x)

except ValueError: 
    print("A value Error is present... please fix it")

except NameError: 
    print("Undeclared variable is being used...Please decare the variables first")

except:
    print("Something unkown went wrong.... Please Fix it")

else: 
    print("Successfull Implementation")

finally:
    print("Try except completed")

x = " Hello "

if type(x) is not int:
    raise Exception("Only Integers are allowed")