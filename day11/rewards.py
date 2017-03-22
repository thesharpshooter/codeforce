a = map(int,raw_input().split(" "))
b = map(int,raw_input().split(" "))
n = int(raw_input())
if (sum(a)%5 == 0) :
	c1 = sum(a)/5
else :
	c1 =sum(a)/5 + 1
if sum(b)%10 == 0 :
	c2 = sum(b)/10
else:
	c2 = sum(b)/10 + 1
if c1 + c2 <= n:
	print "YES"
else:
	print "NO"

