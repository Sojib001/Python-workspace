
# print("Hello World", 7*7)
# print(5)

# print("I'm a good boy")
# print("Hi, there!")
# print("I'm a good boy\nHi, there!")

# # commenting

# print("HI", 5 ,6 , sep = "~", end = " ended ") # by default end = '\n'
# print("ok")

# a = 3
# print(type(a))
# a = "Sojib"
# print(type(a))
# print(a)
# c = complex(4,5);
# print(type(c))
# print(c)

# print(5**3)
# print(5/3)
# print(5//3)

# a = "2"
# b = "1"
# print(int(a)  + int(b)) # the conversion has to be valid or else it will result in an error

# a = input()
# b = input()
# print(int(a) + int(b))

# a = "He said, "
# b = "\"I wasn\'t ready\""
# print(a + b)

# a = '''Hi there!
# I am learning python
# howdy?
# '''
# print(a)
# print(a[0])
# for x in a:
#     print(x)
# print(a[0 : 6])
# print(len(a))
# print(a.upper())
# print(a.lower())
# a = "hello!!!!"
# print(a.rstrip('!'))
# print(a.replace("hello", "Hi"))
# print(a)
# print(a.split("e"))
# print(a.capitalize())
# print(a.center(100, "*"))
# print(a.count("H"))
# print(a.endswith("H"))
# print(a)
# print(a.endswith("e", 0, 2))

x = int(input())
if(x > 18):
    print("Greater than 18!")
    print("You can drive.")
elif(x >= 15):
    print("Just wait for 3 more years.")
else:
    print("Immature!")