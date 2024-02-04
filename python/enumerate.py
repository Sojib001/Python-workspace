list = [1, 2, 3, 4, 5]
for index, num in enumerate(list):
    print(num , end=" ")
    print(index)
for index, num in enumerate(list, start= 1):
    print(num , end=" ")
    print(index)