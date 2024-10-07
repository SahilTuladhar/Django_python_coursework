x = 2321

x = str(x)

reversed_x = x[0:4:1]

print(reversed_x)

list_x = []

for i in range(0, len(x)):
    list_x.append(x[i])

print(list_x)

list_x.reverse()

print(list_x)

rev_string = ""

for char in list_x:
    rev_string = rev_string + char

print(rev_string)
    


