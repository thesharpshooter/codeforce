temp = map(int,raw_input().split(" "))
arr = map(int,raw_input().split(" "))
n = temp[0]
target = temp[1]
i = 0
visited = []
if arr == [1]*(n-1):
    print "YES"
else :
    while i < n-1:
        pos = arr[i] + i+1
        visited.append(i)
        i = pos-1
        if pos == target:
            print "YES"
            break
        if pos in visited :
            print "NO"
            break
    if pos >= n and target != n:
        print "NO"

