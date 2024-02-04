# with normal strings:
string = "My name is {}, I am from {}!"
name = "Sojib"
country = "Bangladesh"
print(string.format(name, country))

# with fstring
# string = f"My name is {name}, I am from {country}!"
print(f"My name is {name}, I am from {country}!")