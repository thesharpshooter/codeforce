x = int(raw_input())
while(True):
    x += 1
    temp = set(list(str(x)))
    if len(temp) == 4:
        break
print x
