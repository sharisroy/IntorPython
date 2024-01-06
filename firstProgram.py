print('Hello world!')

name = "Haris Chandra Roy"

print(name)

sentance, age = "Welcome Bangladesh", 52

print(age, name)
print(name[0])
print(name[0:5])
print(name[:5])
print(name[5:])

# Placeholders in Strings
info = "%s and age is %d"
print(info %(name, 30))

# Format string
print(f"Name :{name}")

a, b = 10,30
print(f"The sum of a and b is {a+b}")
# use this format method for different data type
print("{} {} {} {} {}".format("The sum of",a,b,"is",a+b))