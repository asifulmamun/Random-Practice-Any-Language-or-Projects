"""
    User Input
"""
anyName = input('Enter anythings : ')
print(anyName, type(anyName))

# multi input
x, y, z = input("Enter a three value: ").split() 
print("Total number of students: ", x) 
print("Number of boys is : ", y) 
print("Number of girls is : ", z)

# Input type assign
anyName = int(input('Enter any Intiger : '))
print(anyName, type(anyName))

anyName = str(input('Enter any String : '))
print(anyName, type(anyName))

anyName = float(input('Enter any Float : '))
print('float Number is: %.4f' %anyName, type(anyName))

"""
    Condition
"""

ifinput = int(input('Enter any number : '))
b = 10
c = 20

if ifinput == b:
    print("The number a and b are equeal")
elif ifinput == c:
    print("The number a and c are equeal")
else:
    print('Nothing Match.')


""" 
    Operation titile(), upper() and lower function.
"""
sentence = input('Enter any sentence : ')
print('Title: ', sentence.title())
print('Upper: ', sentence.upper())
print('Lower: ', sentence.lower())