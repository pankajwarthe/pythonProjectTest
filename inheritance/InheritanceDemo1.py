class Base:

    def baseMethod(self):
        print("Base class method called")


class Child(Base):
    def childMethod(self):
        print("Child class method called")

c = Child()
c.childMethod()
b = Base()
b.baseMethod()