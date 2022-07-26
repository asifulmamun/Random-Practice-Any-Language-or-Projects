myint = 12
myfloat = 10.50
mystring = 'This is my string.'
print('%s This float: %.2f, This int: %d' %(mystring, myfloat, myint))
print('%x' %(myint)) # hexadecimal


# string formating str.formate()
mystrformate = 'Hellow {}'
print(mystrformate.format('World'))

# multi string formate
multistring = 'Hello this is {}, This is {}, I love my {}'
print(multistring.format('Bangladesh', 'my area', 'country'))

# inline string formate
print('Hello this is {}, This is {}, I love my {}'.format('Bangladesh', 'my area', 'country'))