# nested while loop
a = 0
b = 0
while a<=10:
    print('This is outer loop', a)
    a+=1
    while b<=15:
        print('inner loop', b)
        b+=1

# # different result
# a = 0
# b = 0
# while a<=10:
#     print('This is outer loop', a)
#     while b<=15:
#         print('inner loop', b)
#         b+=1
#     a+=1


# # nested for loop
# for a in range(3):
#     print('This is Outer loop', a)
#     for b in range(4):
#         print('inner loop', b)

# # different result
# for a in range(3):
#     for b in range(4):
#         print('inner loop', b)
#     print('This is Outer loop', a)

# # differennt
# a = 0
# while a<=10:
#     for b in range(5):
#         print('inner loop', b)
#     print('This is outer loop', a)
#     a+=1

# # differennt
# a = 0
# for b in range(5):
#     print('this is outer loop', b)
#     while a<=10:
#         print('inner loop', a)
#         a+=1

# nested condition
name = input('Enter you name: ')
if name == 'mamun':
    mobile = input('Enter you mobile number: ')
    if mobile == '01721600688':
        print('Log in success.!')
    else:
        print('Mobile Number not mathed.')
else:
    print('You are not memeber of this platform.')