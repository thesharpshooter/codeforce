n = int(raw_input())
a = map(int,raw_input().split(" "))
base = [0]*max(a)
for i in range(len(base)):
    temp = map(lambda x: x>i,a)
    base[i] = temp.count(True)
new = [0]*n
for i in range(0,len(base)):
    for j in range(0,n):
        if base[i] >0:
            new[n-j-1] += 1
            base[i] -= 1
        else:
            new[n-j-1] += 0
for x in new:
    print x,
