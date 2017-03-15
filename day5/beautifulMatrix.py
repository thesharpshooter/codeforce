from math import fabs
n = 5
matrix = []
for i in range(5):
    temp = map(int,raw_input().split(" "))
    if 1 in temp:
        p = i
        q = temp.index(1)
print int(fabs(2-p)+fabs(2-q))
