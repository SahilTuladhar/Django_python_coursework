list1 = [ 1 , 2 , 3, 4, 5]

list2 = [ 'apple' , 'carrot' , ' banana' , 'litchi']

list3 = [ 6,2,5,3,1,9]

list4 =[]

list1.extend(list2)

print(list1)

list2.append("strwaberry")

print(list2)

list2.insert( 1 , 'watermelon')

print(list2)

print(list2.index('apple'))

list4 = list3.copy()

list4.sort()

print(list4)

list2.reverse()

print(list2)