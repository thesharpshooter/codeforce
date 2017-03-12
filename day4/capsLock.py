s = raw_input()
score = [x.isupper() for x in s]
q1 = [True]*len(s)
q2 = [False]+[True]*(len(s)-1)
if score == q2:
    print s[0].upper()+s[1:].lower()
elif score == q1:
    print s.lower()
else:
    print s
