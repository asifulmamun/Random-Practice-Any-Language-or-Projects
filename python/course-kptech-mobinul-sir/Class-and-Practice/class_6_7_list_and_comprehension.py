# lsit function
mylist = ['mamun', 'salehin', 'preoshi', 'sruti', 'borshon', 'shishir', 'rafi']
print('List : ', mylist)

mylist.append('zayed')
mylist.append('limon')
print('aopend : ', mylist)

mylist.insert(9, 'arafat')
print('insert : ', mylist)

mylist.pop()
print('pop : ', mylist)

nextlist = ['arafat', 'poltu']
mylist.extend(nextlist)
print('extend : ', mylist)

mylist.remove('poltu')
print('remove poltu : ', mylist)

print('len ', len(mylist))

print('index borshon: ', mylist.index('borshon'))

mylist.insert(4, 'borshon')
print('inserted borshon in index 4: ', mylist)
print('count borshon how many: ', mylist.count('borshon'))

mylistcopy = mylist.copy()
mylistcopy.pop()
print('not effect mylist affacted only mylistcopy: ', mylistcopy)
print('checking mylist not effect: ', mylist)

mylist.reverse()
print('reverse : ', mylist)

mylist.pop()
print('pop : ', mylist)

mylist.append('mamun')
print('append : ', mylist)

mylist.reverse()
print('reverse : ', mylist)

mylist.sort()
print('sort : ', mylist)

mylist.pop()
print('pop : ', mylist)

mylist.append('zayed')
print('append : ', mylist)

mylistcopy.clear()
print('clear mylistcopy : ', mylistcopy)

del mylist[:3]
print('del first 3 : ', mylist)

del mylist[:]
print('del all : ', mylist)

# loop store in list
square = []
for var in range(10):
    square.append(var)
print(square)

# list comprehension
listCom = [value for value in range(10)]
print(listCom)

# slicing
print('Print without first 3 by slicing: ', mylist[3:])