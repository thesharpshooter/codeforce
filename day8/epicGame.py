temp = map(int,raw_input().split(" "))
a = temp[0]
b = temp[1]
n = temp[2]
def gcd(x,y):
    if x == 0 or y == 0:
        return 0
    if x == y:
        return x
    if x > y :
        return gcd(x-y,y)
    return gcd(x,y-x)
player = 1
while n>0 :
    if player == 0:
        player = 1
    else:
        player = 0
    t = gcd(temp[player],n)
    n -= t
print player
