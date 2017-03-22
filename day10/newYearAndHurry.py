temp = map(int,raw_input().split(" "))
n = temp[0]
k = temp[1]
for i in range(n,-1,-1):
	if ((5*i*(i+1))/2.0 + k) <= 4*60.0:
		break
print i 
