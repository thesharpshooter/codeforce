temp = map(int,raw_input().split(" "))
n = temp[0]
m = temp[1]
a = temp[2]
b = temp[3]
if (n%m)*a >= b:
    x = (n/m)*b + b
    if x < a*n:
        print x
    else:
        print a*n
else:
    x =  (n/m)*b + (n%m)*a
    if x < a*n :
        print x
    else:
        print a*n
