

try:
    marks = 10
    a = marks / 0
    print(a)
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')


x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")
