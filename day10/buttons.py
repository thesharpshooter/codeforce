n = int(raw_input())
i = 1
count = 0
while n-i >= 0:
	count += (n-i)*i + 1
	i += 1
print count

