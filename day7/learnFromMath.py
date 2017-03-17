from math import sqrt
n = int(raw_input())
def is_composite(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i == 0:
            return True
    return False
for i in range(2,n/2+1):
    if is_composite(i) and is_composite(n-i):
        print i," ",n-i
        break

