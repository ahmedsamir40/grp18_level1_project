# program to write into text file
"""
1 - open for write
2 - operation ( write)
3 - close file
"""
my_file = open('C:\\MY_FILES\\write_data.txt','w')
my_file.write('i like football\n')
my_file.write('i like programming\n')
my_file.write('python is a programming language')
my_file.close()
print('--- second way ----')
with open('C:\\MY_FILES\\write_data.txt','a') as f:
    f.write('\n++++++++++++++++++\n')
    f.write('python is the basic programming for AI\n ')
    f.write('You should learn Django for python backend development')

