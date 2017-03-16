num = map(int,raw_input().split(" "))
temp = map(int,raw_input().split(" "))
temp = sorted(temp)
size = [temp[i+num[0]-1] - temp[i] for i in range(num[1]-num[0]+1)]
print min(size)
