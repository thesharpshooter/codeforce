n = int(raw_input())
a = map(int,raw_input().split(" "))
b = 0
count = 0
for x in a:
	if x != -1:
		b += x
	elif x == -1 and b == 0:
		count += 1
	elif x == -1:
		b -= 1
print count
