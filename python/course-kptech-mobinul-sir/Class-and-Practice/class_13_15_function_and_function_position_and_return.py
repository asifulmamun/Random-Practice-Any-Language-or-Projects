# # some built in function math
# a = 10
# print(bool(a))
# print(bin(a))
# print(hex(a))
# print(hash(a))
# print(pow(a, 2))
# print(abs(a))


# # some string function upper(), str(), len() and input() etc
# text = 'This is text'
# text = set(text) # converting set
# print(text, type(text))
# print(len(text))


# # User defing function
# def myfunction():
#     return 'This is my function'
# print(myfunction()) # call function


# def myfunction2():
#     print('This is my function')
# myfunction2() # call function


# def mathfunction(a, b):
#     print(a+b)
#     print('%d is first number and %d is seconde number'%(a, b))
# mathfunction(5,6) # call function

# def feel(fruit, size):
#     print('This is %s, This size is %s'%(fruit, size))
# feel('mango', 'small') # define print

# def feel(fruit, size = 'small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel('mango') # pre define print

# def feel(fruit, size):
#     print('This is %s, This size is %s'%(fruit, size))
# feel(fruit = 'mango', size = 'small') # define print

# def feel(fruit, size = 'small'):
#     print('This is %s, This size is %s'%(fruit, size))
# name = 'mango'
# feel(name, 'medium') # define var print and change var pre define

# def feel(fruit, size):
#     print('This is %s, This size is %s'%(fruit, size))
# feel(fruit='mango', size='medium') # define print

# def feel(fruit='lichi', size='small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel(fruit='mango', size='medium') # pre define change

# def feel(fruit='lichi', size='small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel(size='medium') # pre define change single

# def feel(fruit='lichi', size='small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel('mango', size='medium') # pre define change single witout define in call

# def feel(fruit, size='small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel('mango') # call single

# def feel(fruit='mango', size='small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel('lichi') # call single

# def feel(fruit='mango', size='small'):
#     print('This is %s, This size is %s'%(fruit, size))
# feel(fruit='lichi') # define call single

# def feel(fruit='mango', size='small'):
#     return 'This is %s, This size is %s'%(fruit, size)
# print('Result : ',feel(fruit='lichi')) # return