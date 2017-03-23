temp = map(int,raw_input().split(" "))
d1 = temp[0]
d2 = temp[1]
d3 = temp[2]
print min(d1,d2)+min(d1+d2,d3)+min(max(d1,d2),min(d1,d2)+d3)
