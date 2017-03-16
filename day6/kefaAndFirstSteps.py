n =int(raw_input())
num = map(int,raw_input().split(" "))
stat = [1]*n
i = 0
for j in range(n-1):
    if num[j+1] >= num[j]:
        stat[i] += 1
    else:
        i += 1
print max(stat)
