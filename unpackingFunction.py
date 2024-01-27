def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total + arg

    return total


print(multiply(1, 2, 3))


# def add(x, y):
#     return x + y
#
#
# nums = [3, 5]
# print(add(nums))


def named(name, age):
    print(name, age)


def detail(**kewargs):
    print(kewargs)


details = {"name": "Haris", "age": 30}
named(**details)
detail(**details)
