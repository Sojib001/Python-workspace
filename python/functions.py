# def calcavg(a, b):
#     print((a+b) / 2)
# def checkgreater(a, b):
#     if(a > b):
#         print("a is greter than b")
#     else:
#         print("b is greater than or equal to a")
# a = int(input())
# b = int(input())
# x = calcavg(a, b)
# checkgreater(a, b)
# print(x)

# def average(*number): # *number denotes a list, if ** is used it becomes a dictionary
#     sum = 0
#     for x in number:
#         sum += x
#     return sum / len(number)
# c = average(1, 2, 3 , 4)
# print(c)

# recursion:

def fact(num):
    if(num == 0):
        return 1
    return num*fact(num - 1)
x = int(input())
print(fact(x))