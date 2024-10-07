mylist = [[ 10 , 21 , 34] , [ 24 , 35 ,56 ] , [77, 83, 39] ]

print(mylist)

for outer in mylist:
    for inner in outer:
        index = mylist.index(outer) + outer.index(inner) + 1
        print('The' , index , "element is" , inner)