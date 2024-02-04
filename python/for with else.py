for i in range(5):
    print(i)
else:
    print("Range is finished")

for i in range(5):
    print(i)
    if(i == 2):
        break
else:
    print("Range is finished") # Now, this won't be printed!