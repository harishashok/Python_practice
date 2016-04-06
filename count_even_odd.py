import random
numbers = random.sample(range(0,1000),100)
odd_count = 0
even_count = 0
for num in numbers:
    if num %2 == 0:
        even_count += 1
    elif num %2 ==1:
        odd_count += 1
print "Total even numbers :", even_count
print "Total odd numbers :", odd_count
