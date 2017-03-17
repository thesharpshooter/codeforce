temp = map(int,raw_input().split(" "))
n =temp[0]
k = temp[1]
if n%2 == 0:
    odd = n/2
    even = n/2
else:
    odd = n/2 +1
    even = n/2
if k <=odd :
    print (2*k - 1)
else:
    print 2*(k-odd)
