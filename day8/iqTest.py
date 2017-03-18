from math import fabs
n = int(raw_input())
temp = map(int,raw_input().split(" "))
diff = []
for i in range(0,n-1):
    x = fabs(temp[i+1] - temp[i])
    diff.append(x)
buff = list(set(diff))
print buff
count1 = diff.count(buff[0])
count2 = diff.count(buff[1])
print "count 1",count1
print "count 2",count2
if count1 < count2 and n > 4:
    even = buff[0]
else:
    even = buff[1]
print "even : ",even
for i in range(0,n-1):
    x = temp[i+1] - temp[i]
    if x == even:
        print i+2
        break
