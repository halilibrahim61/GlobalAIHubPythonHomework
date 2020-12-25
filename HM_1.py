mylist = []
v = int(input("Please enter how many values you will take :" ))

for i in range(0, v):
 value = input(f'{i}th value is ')
 if value.isdigit():
  mylist.append(int(value))
 else:
  mylist.append(value)   
 print(mylist)
print(f'List type is {type(mylist)}.')
