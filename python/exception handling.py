try:
    a = int(input("Enter a number: "))
    for x in range(1, 11):
        print(f"{x} X {a} = {x * a}")
except Exception as e: # except: print("Wrong")
    print(e)

# except ValueError:
    #print("Value Error")
# except IndexError:
    #print("Index Error")

