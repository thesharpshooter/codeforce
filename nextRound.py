#participants who got selected for the next round

n, k = map(int,raw_input().split(" "))
scores = list(map(int, raw_input().split(" ")))
#print scores
threshold = scores[k-1]
count = 0
for x in scores :
    if x >0 and x>= threshold :
        count += 1
print count
