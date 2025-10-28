
class class_A:
    def method_A(self):
        print("Method of Class A called")

class class_B(class_A):         # Class B inherits from Class A
    def method_B(self):
        print("Method of Class B called")

class class_C(class_B):         # Class C inherits from Class B
    def method_C(self):
        print("Method of Class C called")


obj1 = class_C()

obj1.method_C()
obj1.method_B()
obj1.method_A()
