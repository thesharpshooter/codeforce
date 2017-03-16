string = raw_input()
score = 0
n = len(string)
for x in string:
    if x.isupper():
        print "before",score
        score += 1
        print 'after',score
print score
if score == 1 or score == n :
    temp = string[0].upper()
    for i in range(1,n):
        temp += string[i].lower()
    print temp
print string

