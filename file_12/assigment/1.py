# read file store numbers in a list and calculate sum and averadge
new_lines_list = []
total =0
with open('C:\\MY_FILES\\assigment\\assi.txt','r') as f:
    lines_list = f.readlines()

    for line in lines_list:
        line = line.strip()
        new_lines_list.append(line)
        total = total + int(line)
        average = total / len(new_lines_list)

print(new_lines_list)
print(total)
print(average)