n = int(raw_input())
temp = []
for i in range(n):
	curr = map(int,raw_input().split(" "))
	if curr[0] > curr[1]:
		temp.append("m")
	elif curr[0] < curr[1]:
		temp.append("c")
M = temp.count("m")
C = temp.count("c")
if M>C:
	print "Mishka"
elif M<C:
	print "Chris"
else:
	print "Friendship is magic!^^"
