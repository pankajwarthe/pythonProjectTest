def print_name(*args):
    print(args)
    print(args[1])

print_name("Pankaj", "Warthe", "Kumar","Singh")
# =========================================

def sum_of_all_num(*args):
    print("sum of all num: "+str(sum(args)))

sum_of_all_num(10,20,30,40,50)
# =========================================

def get_max_num(*args):
    print(max(args))

get_max_num(100,200,300,400,500,600)
# =========================================

def get_min_num(*args):
    print(min(args))

get_min_num(1000,2000,3000,4000,5000,6000)
# =========================================