def sum(a, b):
    print(a + b)


sum(5, 6)


def fullName(first, last):
    return first + last


name = fullName("Haris Chandra", "Roy")
print(name)

i = 5


def f(arg=i):
    print(arg)


i = 6
f()

"""Print a Fibonacci series up to n."""


def fib(n):  # write Fibonacci series up to n

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(200)


def concat(*args, sep="/"):
    print(sep.join(args))


concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

