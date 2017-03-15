temp = map(int,raw_input().split(" "))
queue = list(raw_input())
for i in range(temp[1]):
    j = 0
    while j<(temp[0] - 1):
        if queue[j] == "B" and queue[j+1] == "G":
            queue[j],queue[j+1] = queue[j+1],queue[j]
            j+=1
        j+=1
print "".join(queue)
