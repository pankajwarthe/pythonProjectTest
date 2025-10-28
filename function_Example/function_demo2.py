def check_even_number(number):

    if number % 2==0:
        print("The number "+ str(number) +" is even.")
    else:
        print("The number "+ str(number) +" is odd.")

check_even_number(13)
#======================================================

def check_even_num_list(list1):
    even_numbers = []

    for num in list1:
        if num % 2==0:
            even_numbers.append(num)
    return even_numbers

result = check_even_num_list([1,2,3,4,5,6,7,8,9,10])
print("Even numbers in the list are: ", result)
#======================================================

def check_odd_num_list(list1):
    odd_numbers = []

    for num in list1:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

result = check_odd_num_list([1,2,3,4,5,6,7,8,9,10])
print("Odd numbers in the list are: ", result)
#======================================================