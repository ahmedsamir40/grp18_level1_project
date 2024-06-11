# program to read from text files
"""
1 - open file for reading
2 - read content and use print to show the content
3 - close file
"""
print('----first way-----')
my_file = open('C:\\MY_FILES\\ahmed\\read_data.txt','r')
content = my_file.read()
print(content)
my_file.close()

print('--- second way using with ignore close() ------')
with open('C:\\MY_FILES\\ahmed\\read_data.txt','r') as my_file2:
    content = my_file2.read()
    print(content)