from math import fabs
n = int(raw_input())
bits = raw_input()
count = 0
for i in range(n):
    if bits[i] == bits[0]:
        count += 1
    else:
        count -= 1
print int(fabs(count))
