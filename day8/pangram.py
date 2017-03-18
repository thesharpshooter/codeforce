n = int(raw_input())
string = list(raw_input().lower())
check = len(list(set(string)))
if check < 26:
    print "NO"
else:
    print "YES"
