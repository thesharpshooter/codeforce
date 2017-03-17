n = int(raw_input())
x = map(int,raw_input().split(" "))
y = map(int,raw_input().split(" "))
p = x[1:]
q = y[1:]
r = set(p + q)
if len(r) == n:
    print "I become the guy."
else:
    print "Oh, my keyboard!"
