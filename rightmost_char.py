S = "HellE CodeEval,E"
index = S.find(",")+1
target = S[index]
string = S[:index-1]
string.rfind(target)

"""
Alternate solution
"""
def rightmost_char(S):
  p = S.strip().split(",")
  print p[0].rfind(p[1])
  
rightmost_char("Hello World,r")  
