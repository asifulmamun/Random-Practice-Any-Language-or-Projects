# With Super Function in child method
class Parent():
    def __init__(self, name):
        self.name = name
    def myDef(self):
        print('From Parent: ', self.name)

class Child(Parent):
    def __init__(self, name):
        # initialize child
        super().__init__(name)

    def childDef(self, area):
        print('From Child: ', area)