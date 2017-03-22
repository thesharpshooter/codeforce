n = int(raw_input())
a = []
b = []
for i in range(n):
	curr = raw_input()
	if curr not in b:
		a.append("OK")
		b.append(curr)
	elif curr in b:	
		b.append(curr)
		curr = curr +str(b.count(curr)-1)
		a.append(curr)
	
for y in a:
	print y
