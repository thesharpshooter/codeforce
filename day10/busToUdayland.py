n = int(raw_input())
temp = []
found = False
for i in range(n):
	curr = raw_input()
	if found == False and (curr[0] =="O" and  curr[1] == "O"):
		curr = "++"+curr[2:]
		found = True
	elif found == False and (curr[-1] == "O" and curr[-2] == "O"):
		curr = curr[:3]+"++"
		found = True
	temp.append(curr)
if found:
	print "YES"
	for x in temp:
		print x
else:
	print "NO"
