n = int(raw_input())
order = map(int,raw_input().split(" "))
dic = {}
for i in range(n):
    dic[order[i]] = i+1
for i in range(n):
    print dic[i+1],
