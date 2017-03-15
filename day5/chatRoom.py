word = raw_input()
check = list("hello")
i = 0
j = 0
count = 0
for i in range(len(word)):
    if j<5 and word[i] == check[j] :
        
        count += 1
        j += 1
    elif j>=5:
        break
if count == 5:
    print "YES"
else:
    print "NO"
