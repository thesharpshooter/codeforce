a = raw_input()
b = raw_input()
a = a.lower()
b = b.lower()
n = len(a)
score1 =  0
score2 = 0
for i in range(n):
    score1 += (10**(n-1-i)) * ord(a[i])
    score2 += (10**(n-1-i)) * ord(b[i])
if score1 > score2:
    print 1
elif score1 == score2:
    print 0
else:
    print -1
