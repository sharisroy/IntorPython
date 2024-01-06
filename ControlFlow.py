# x = int(input("Please enter an integer: "))
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

    # For Loop

obj = [1, 2, 3, 4, 5, 6]
for i in obj:
    print(i, end=' ')

# print 1 to 10
for j in range(1, 10):
    print(j, end=' ')
# print 1 4 7 10 (interval 3)
for j in range(1, 11, 3):
    print(j, end=' ')

# Measure some strings:
words = ['cat', 'window', 'Haris Chandra Roy']
for w in words:
    print(w, len(w))  # print the length of item

# Create a sample collection
users = {'Haris': 'active', 'Kumar': 'inactive', 'Jibon': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    print(status)
    if status == 'inactive':
        del users[user]
print(users)  # print only active user
# print(users.copy().items())


# While Loop
n = 4
while n > 1:
    print(n, end=' ')
    n = n - 1

n = 40
while n > 1:
    if n % 4 == 0:
        print(n, end=' ')
    n = n - 1



test = "test variabl;e"