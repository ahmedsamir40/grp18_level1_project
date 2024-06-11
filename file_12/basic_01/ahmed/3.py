# program to read from a file and write to another file
with open('C:\\MY_FILES\\ahmed\\read_data.txt','r') as f:
    content = f.read()
with open("C:\\MY_FILES\\ahmed\\write_data2.txt", 'w') as f:
    f.write(content)