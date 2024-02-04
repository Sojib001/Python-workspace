# ages = [3, 6, 5, "sojib"]
# print(ages)
# print(type(ages))
# print(ages[0])

# if "sojib" in ages:
#     print("Yes")
# print(ages[1:3])

# auto_list = [i for i in range(4)]
# print(auto_list)

# auto_list = [i*i for i in range(10) if i%2 == 0 and i%3 == 0]
# print(auto_list)

list  = [1, 20, -3, 100]
# list.reverse()
# print(list)
# list.sort()
# print(list)
# list.sort(reverse = 1)
# print(list)
# list.append(9)
# print(list.count(1))
# list.insert(1, -100)
# print(list.index(1))

# m = list
# m[0] = 2
# print(m)
# print(list)
m = list.copy()
m[0] = 2
print(m)
print(list) 
list.extend(m)
print(list)
list = list + m
print(list)


