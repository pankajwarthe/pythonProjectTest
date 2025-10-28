class Person:

    def welcome(self):      # this is a method of the Person class
        print("Welcome to the OOPS in Python")

    def hello_world(self):  # this is another method of the Person class
        print("Hello, World! from OOPS")

    def cal_sum(self, a, b):
        print("sum= ",a + b)

def not_class_method():   # this is a regular function, not part of the Person class
    print("This is not a class method")



obj = Person()
obj.welcome()           # calling method from Person class
obj.hello_world()       # calling another method from Person class

not_class_method()      # calling a regular function which is not part of the Person class

obj.cal_sum(5, 10)      # calling cal_sum method from Person class
