n = int(raw_input())
temp = [1]
i = 1
n = n-1
while True:
    curr = temp[i-1]+i+1
    if n >= curr :
        temp.append(curr)
        n -= curr
        i +=1
    else:
        break
print len(temp) 
