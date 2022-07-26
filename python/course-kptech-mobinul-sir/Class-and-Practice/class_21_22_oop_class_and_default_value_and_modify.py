# # simple method and property and create obj
# class Myclass():
#     name = 'mamun'
#     age = 22

#     def myfunction(self):
#         print('My name is', self.name)
#         print('My age is', self.age)

# print(Myclass().name)
# myObj = Myclass()
# print(myObj.name)
# print(myObj.myfunction())



# # argument pass by method
# class Myclass():

#     def myfunction(self, name, age):
#         print('My name is', name)
#         print('My age is', age)

# myObj = Myclass()
# print(myObj.myfunction('mamun', 22))



# # in init function and object argument pass
# class Myclass():
#     def __init__(self, name):
#         self.name = name

#     def myDef(self):
#         print('Hello', self.name)

# myObject = Myclass('mamun')
# myObject.myDef()



# # in init function and object argument pass
# class Myclass():
#     def __init__(self, name):
#         self.name = name

#     def myDef(self, age):
#         print('Hello', age)

# myObject = Myclass('mamun')
# print(myObject.name)
# myObject.myDef(22)



# # Default Value and modify them when call
# class Myclass():
#     def __init__(self, name):
#         self.name = name
#         self.area = 'kg'

# myObject = Myclass('mamun') # not need
# print(myObject.area)
# myObject.area = 'Kishoregaj'
# print(myObject.area)