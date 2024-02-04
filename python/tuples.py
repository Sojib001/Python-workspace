# tup = (1, "green", 3, True) # cant change the values after creation!
# print(tup)
# print(tup[0])

tup = (1, 2, 3, 4, 5, 5)
temp = list(tup)
temp.append(8)
temp.pop(4) # pops index 4
print(temp)
tup = tuple(temp)
print(tup)

tup.count(3)
tup.index(3)
len(tup)
