"""Write a Python program to count the number of strings where the 
string length is 2 or more and the first and last 
character are same from a given list of strings."""
def count_string(s):
    count = 0
    while len(s)>=2:
        for i in s:
            if i[0] == i[-1]:
                count += 1
        return count
s = ['abc', 'xyz', 'aba', '1221']

count_string(s)
