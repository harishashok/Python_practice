a = int(raw_input("Enter a number"))

visited = set()
while 1:
    if a == 1:
        print "Happy number"
        break
    a = sum(int(x) **2 for x in str(a))
    if a in visited:
        print "Sad Number"
        break
    visited.add(a)
