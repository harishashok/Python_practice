#Write a Python program to sum all the items in a list. 

num = [10,33,484,494,39]

def sum_list(num):
    total = 0
    for i in num:
        total += i
    return total

sum_list(num)


#Write a Python program to multiplies all the items in a list.

num1 = [10,3,84,4,39]

def product_list(num1):
    total = 1
    for i in num1:
        total *= i
    return total

product_list(num1)
