# program ro read from text file and put data into list
new_lines_list = []
with open('C:\\MY_FILES\\ahmed\\read_data.txt','r') as f:
    lines_list = f.readlines()
    for line in lines_list:
        line = line.strip()  # remove \n
        if line != '':   # remove any empty line
            new_lines_list.append(line)
print(new_lines_list)