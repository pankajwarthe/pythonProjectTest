class Person:


    def __init__(self, fname, lname):  # Parameterized Constructor
        self.fname = fname
        self.lname = lname
        print("Parameterized Constructor called " + fname + " " + lname)

if __name__ == "__main__":
        # Demo: create a Person using the parameterized constructor
        p = Person("John", "Doe")
        print("p attributes:", p.fname, p.lname)


    def sumOf(self, a, b):
        self.v1 = a
        self.v2 = b
        return self.v1 + self.v2




