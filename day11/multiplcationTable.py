def getDiv(x):
	div = []
	for i in range(1,n+1):
		if x%i == 0:
			div.append(i)
	return div
temp = map(int,raw_input().split(" "))
n = temp[0]
x = temp[1]
count = 0
for z in getDiv(x):	
	if z <= n and (x/z) <= n:
		count += 1
print count
