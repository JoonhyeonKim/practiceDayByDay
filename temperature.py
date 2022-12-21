import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
p = []
n = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t < 0:
        a = abs(t)
        n.append(a)
    else:
        p.append(t)

p.sort()
n.sort()
if p==[] and n==[]:
    print(0)
elif p==[] and n!=[]:
    print(-n[0])
elif p!=[] and n==[]:
    print(p[0])
else:
    if p[0]>n[0]:
        print(-n[0])
    else:
        print(p[0])
