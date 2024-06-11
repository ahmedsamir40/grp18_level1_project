print('====program to reverse words of string ----')
statement = 'i like this program very much'

#coveert string to a list  using (split)
words_list = statement.split()
words_list.reverse()
print(words_list)

# covert the list back to string
statement = ' '.join(words_list)
print(statement)