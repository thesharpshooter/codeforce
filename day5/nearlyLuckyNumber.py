num = raw_input()
lucky_number = ['4','7']
count = 0
for x in num:
    if x in lucky_number:
        count += 1
if str(count) in lucky_number:
    print "YES"
else:
    print "NO"
