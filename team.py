#Problems solved in a programming test

n = int(raw_input())
count = 0 
while (n > 0 ):
    temp = 0
    status = list(map(int, raw_input().split(" ")))
    for x in status :
        if x == 1:
            temp += 1
    if temp >= 2 :
        count += 1
    n -= 1

print count
