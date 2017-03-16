n = int(raw_input())
if n%2 == 0:
    s1 = (n/2)*(1+ n-1)
    s2 = (n/2)*(2 + n)
    print (s2 - s1)/2
else:
    s1 = (n/2 + 1)*(1 + n)
    s2 = (n/2)*(2 + n-1)
    print (s2-s1)/2
