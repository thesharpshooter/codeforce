temp = map(int,raw_input().split(" "))
n = temp[0]
m = temp[1]
x = "#"*m
y = "."*(m-1)+"#"
curr = y
for i in range(n):
    if curr == x :
        curr = y
    else:
        curr = x
    if curr == y:
        print y
        y = y[::-1]
    else:
        print curr
