a = list(raw_input())
b = list(raw_input())
res = ""
for i in range(len(a)):
    if a[i] != b[i]:
        res += "1"
    else:
        res += "0"
print res
