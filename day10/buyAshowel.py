temp = map(int,raw_input().split(" "))
k = temp[0]
r = temp[1]
i = 1
while True :
	if ((i*k)%10 == 0) or (i*k == r) or ((((i*k)%10)-r) == 0):
		break
	i += 1
print i
