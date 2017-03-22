temp = map(int,raw_input().split(" "))
found = False
for i in range(temp[1],temp[0]+1,temp[1]):
	p = 2*i - temp[0]
	if p >= 0 :
		found = True
		break
if found :
	print i
else:
	print -1
