#Write a Python program to get the largest number from a list
num2 = [10,3,84,4,39]

def greater_num(num2):
    max = num2[0]
    for i in num2:
        if i>max:
            max = i
    return max

greater_num(num2)
        
#Alternate solution using max function
max(num2,key = int)
