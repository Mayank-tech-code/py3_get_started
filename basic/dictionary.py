dict_students = {1: 'rohit', 2: 'prakash', 3: 'adinath'}
print(dict_students)

dict_students[4] = 'nisar'
dict_students[5] = 'varsha'
dict_students[6] = 'divya'
print(dict_students)

del dict_students[5]
print(dict_students)

for key in dict_students:
    print(key)
    print(dict_students[key])