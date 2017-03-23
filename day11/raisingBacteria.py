n = int(raw_input())
def getBinary(n):
    temp = []
    while n >0:
        temp.append(n%2)
        n = n/2
    temp.append(n/2)
    return temp

print getBinary(n).count(1)


