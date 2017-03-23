n = int(raw_input())
total = 0
curr = 1000
for i in range(n):
    temp = map(int,raw_input().split(" "))
    price = temp[1]
    meat = temp[0]
    if price < curr:
        curr = price
    total += curr*meat
print total
