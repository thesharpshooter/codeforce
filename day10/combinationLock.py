from math import fabs
n = int(raw_input())
value = raw_input()
curr = raw_input()
count = 0
for i in range(n):
	val1 = fabs(int(value[i])-int(curr[i]))
	val2 = 10 - max(int(value[i]),int(curr[i])) + min(int(value[i]),int(curr[i]))
	count += min(val1,val2)
print int(count)
