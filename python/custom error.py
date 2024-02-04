x = int(input("Enter a number: "))
if(type(x) == str):
    raise ValueError("Value is string")
if(x < 5 or x > 9):
    raise ValueError("Value must be in between 5 and 9.")

# search python error classes