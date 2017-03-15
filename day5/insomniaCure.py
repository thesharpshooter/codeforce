temp = []
for i in range(4):
    x = int(raw_input())
    temp.append(x)
n = int(raw_input())
dragons = n
if 1 in temp:
    print n
else:
    for i in range(1,n+1):
        if i%temp[0] != 0 and i%temp[1] != 0 and i%temp[2] != 0 and i%temp[3]!=0:
            dragons -=1
    print dragons
