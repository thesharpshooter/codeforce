n = int(raw_input())
point = map(int,raw_input().split(" "))
count = 0
for i in range(1,n):
	if point[i] > max(point[:i]) or point[i] < min(point[:i]):
		count += 1
print count 
