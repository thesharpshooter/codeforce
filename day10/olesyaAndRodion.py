temp = map(int,raw_input().split(" "))
n = temp[0]
t = temp[1]
found = False
i = 10**(n-1)
while i < 10**(n):
	if i % t == 0 :
		found = True
		break
	i+=1
if found :
	print i
else:
	print -1
