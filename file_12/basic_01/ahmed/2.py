# program to read from text files
"""
1 - open for write
2 - operation ( write)
3 - close file
"""
print('-------first way----')
my_file = open("C:\\MY_FILES\\ahmed\\write_data.txt",'w')
my_file.write('I like football\n')
my_file.write('I like programming\n\n')
my_file.write('Python is a programming language')
my_file.close()

print('-----second way ------')
with open("C:\\MY_FILES\\ahmed\\write_data.txt",'a') as f:
    f.write('\n')
    f.write('python is the basic programming for AI\n ')
    f.write('You should learn Django for python backend development')
