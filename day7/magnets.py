n = int(raw_input())
temp = []
group = 1
for i in range(n):
    curr = raw_input()
    temp.append(curr)
    if i >0:
        if curr != temp[i-1]:
            group += 1
print group
