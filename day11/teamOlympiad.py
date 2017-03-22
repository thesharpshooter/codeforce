n = int(raw_input())
a = map(int,raw_input().split(" "))
temp = []
while a != [-1]*n:
	curr = []
	for i in range(1,4):
		if i not in a:
			break
		index = a.index(i)
		curr.append(index+1)
		a[index] = -1
	if len(curr) == 3:
		temp.append(curr)
	if len(curr) != 3:
		break
print len(temp)
for x in temp:
	for y in x:
		print y,
	print ""
