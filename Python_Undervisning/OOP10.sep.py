class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("destructor")

    def showNAme(self):
        print(self.name)

a = Person("Bob")

a.showNAme()




class A:

    x = []

    def add(self):
        self.x.append(1)

class B:
    def __init__(self):
        self.x = []


    def add(self):
        self.x.append(1)

x = A()
y = A()
x.add()
y.add()
print("A's X:",x.x)

print("B's X:",y.x )


