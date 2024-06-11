book_dict = {'pages':'227', 'name':'gone girl','year': 2007 }

book_dict['author'] = 'well max'
print(book_dict)
print(book_dict['name'])
book_dict['year'] = book_dict['year'] + 3
print(book_dict)
for key, value in book_dict.items():
    print(key,value)
book_dict.pop('name')
print(book_dict)

