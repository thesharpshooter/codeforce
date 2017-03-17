n = int(raw_input())
arr = map(int,raw_input().split(" "))
l = max(arr)
s = min(arr)
for i in range(n):
    if arr[i] == l:
        break
for j in range(n):
    if arr[n-j-1] == s:
        break
pos_min = n-j-1
pos_max = i
if pos_max < pos_min :
    print pos_max + n-1 - pos_min
else:
    print pos_max + n-1 - pos_min - 1
