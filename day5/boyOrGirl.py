user = list(raw_input())
temp = []
for x in user:
    if x not in temp:
        temp.append(x)
if len(temp)%2 != 0:
    print "IGNORE HIM!"
else:
    print "CHAT WITH HER!"
