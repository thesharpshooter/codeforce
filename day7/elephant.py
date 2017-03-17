n = int(raw_input())
steps = [5,4,3,2,1]
count = 0
for x in steps:
    if n >= x:
        count += n/x
        n = n%x
print count
