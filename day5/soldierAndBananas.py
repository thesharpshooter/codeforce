temp = map(int,raw_input().split(" "))
price = temp[0]
money = temp[1]
bananas = temp[2]
cost = 0
for i in range(1,bananas+1):
    cost += price*i
if cost > money :
    print cost - money
else:
    print 0
