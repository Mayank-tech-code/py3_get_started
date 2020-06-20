names = ['prakash','rohit','adinath']
print("Printing names list",names)

for name in names:
    print('Print name in first for loop: ',name)

for i in range(0,len(names)):
    print('Print name in second for loop: ',name)

names.append('nisar')
names.append('divya')
print(names)

del names[0]
print(names)

names.pop()
print(names)
