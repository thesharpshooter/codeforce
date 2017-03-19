temp = map(int,raw_input().split(" "))
s = temp[0]
n = temp[1]
dragons = []
for i in range(n):
    curr = map(int,raw_input().split(" "))
    dragons.append(curr)
dragons.sort(key = lambda tup:tup[0])
for x in dragons :
    if s > x[0]:
        s += x[1]
    if s <= x[0]:
        print "NO"
        break
if s > x[0]:
    print "YES"
