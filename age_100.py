import datetime
name = raw_input("Enter your name:\n ")
p_age = int(raw_input("Enter your age: "))
curr_year = datetime.datetime.now().year
f_year = (100 - p_age) + curr_year
print "Hello Mr %s, your current age is %d and you will turn 100 in the year %d" % (name, p_age, f_year)
