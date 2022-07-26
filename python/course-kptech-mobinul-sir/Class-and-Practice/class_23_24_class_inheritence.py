# class Parent():
#     def __init__(self, name):
#         self.name = name
#     def myDef(self):
#         print('Hello', self.name)

# class Child(Parent):
#     def childDef(self):
#         print('This is from child. Name is: ', self.name)

# myObject = Child('Mamun')
# myObject.myDef()
# myObject.childDef()




# # With Super Function in child method
# class Parent():
#     def __init__(self, name):
#         self.name = name
#     def myDef(self):
#         print('From Parent: ', self.name)

# class Child(Parent):
#     def __init__(self, name):
#         # initialize child
#         super().__init__(name)

#     def childDef(self, area):
#         print('From Child: ', area)

# myObject = Child('Mamun')
# myObject.myDef()
# myObject.childDef('kishoreganj')




# # With Super Function in child method
# class Parent():
#     def __init__(self, name):
#         self.name = name
#     def myDef(self):
#         print('From Parent: ', self.name)

# class Parent2():
#     myname = 'haque'

# class Child(Parent):
#     def __init__(self, name):
#         # initialize child
#         super().__init__(name)
#         self.parent2 = Parent2()

# myObject = Child('Mamun')
# myObject.myDef()
# print(myObject.parent2.myname)
