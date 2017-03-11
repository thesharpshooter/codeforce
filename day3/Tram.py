stops = int(raw_input())
a = [0]*stops
b = [0]*stops
p = [0]*stops
for i in range(stops):
    a[i],b[i] = map(int,raw_input().split(" "))
    if i == 0:
        p[i] = b[i]
    elif i == stops-1:
        p[i] == a[i]
    else:
        p[i] = p[i-1] - a[i] + b[i]
print max(p)

