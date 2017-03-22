n = int(raw_input())
temp = list(raw_input())
a = temp.count("A")
d = temp.count("D")
if a > d:
	print "Anton"
elif a < d :
	print "Danik"
else:
	print "Friendship"
