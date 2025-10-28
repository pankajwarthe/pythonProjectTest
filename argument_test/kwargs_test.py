def print_name(**kwargs):
    print(kwargs)
    print(kwargs['lname'])
    print(type(kwargs))

print_name(fname="Pankaj", lname="Warthe", mname="Kumar", surname="Singh")

# =========================================

def hello_world(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

hello_world(10, 20, name="Pankaj", lname="Warthe")

# =========================================

def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")