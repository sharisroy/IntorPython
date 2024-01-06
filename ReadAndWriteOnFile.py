# Open file
import os.path

f = open(r'File/read.txt')
# print(f.read()) # print full file
# print(f.read(10)) # print n character
# print(f.readline()) # print line by line
# print(f.readlines()) # print all lines
# print(f.readable()) # print readable or not

# read nth line from the file
# content = f.readlines()
# print(len(content)) # print line number
# print(content[5])

# print first 3 lines of file
# print(content[0:3])

# print file all info
# char_count = 0
# word_count = 0
# space_count = 0
# line_count = 0
# for line in f.readlines():
#     # print(line) # print all lines using loops
#     line_count += 1
#     char_count += len(line)
#     words = line.split()
#     word_count += len(words)
#     space_count += len(words) - 1
#
# print("File analysis summary:")
# print("Character count:", char_count)
# print("Word count:", word_count)
# print("Space count:", space_count)
# print("Line count:", line_count)
# print("File size is", os.path.getsize('File/read.txt'), "bytes")


# Write on file

with open('File/write.txt', 'w') as the_file:
    the_file.write("writing on file....\n")
    for line in f.readlines():
        the_file.write(line)

f.close()
