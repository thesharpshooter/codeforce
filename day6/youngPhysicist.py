n = int(raw_input())
force = [0,0,0]
for i in range(n):
    temp = map(int,raw_input().split(" "))
    force[0] += temp[0]
    force[1] += temp[1]
    force[2]+= temp[2]
    
if force == [0,0,0]:
    print "YES"
else:
    print "NO"
