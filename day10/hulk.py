n = int(raw_input())
feel = ["love",'hate']
s = ""
for i in range(1,n+1):
	if i != n:
		s += "I "+feel[i%2]+" that "
	else :
		s += "I "+feel[i%2]+" it"
print s
