temp = map(int,raw_input().split(" "))
a = sorted(list(set(temp[1:])))
n = temp[0]
count = 0
if len(a) == 1 :
	count == n/a[0] 
while n > 0 :
	for i in range(len(a)-1):
		if n%a[i] == 0 or (n > a[i+1] and n%a[i+1] != 0):
			curr = a[i]
			break
	print "Curr i",i
	print "Curr : ",curr
	print "N before : ",n
	n -= curr
	print "N after : ",n
	count += 1
	print "Count : ",count
print count

