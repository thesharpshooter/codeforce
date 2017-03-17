temp = map(int,raw_input().split(" "))
n = temp[0]
m = temp[1]
day = 1
socks = n
while socks > 0:
    if day%m == 0:
        socks = socks
    else :
        socks = socks-1
    day += 1
print day-1
