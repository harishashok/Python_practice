#Print entire string in reverse order

s = "Hello this is a recursive program"
p = s.split(' ')
index = len(p)
string = ''
for i in p:
    while index >0:
        string += p[index-1] + ' '
        index -= 1
print string
