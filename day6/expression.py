from math import fabs
num = []
score = 0
for i in range(3):
    x = int(raw_input())
    num.append(x)
if 1 not in num:
    score = num[0]*num[1]*num[2]
else:
    check = map(lambda x :True if x == 1 else False,num)
    if check == [True,False,False] or check == [False,False,True]:
        score = (1 + num[1])*num[int(fabs(2-check.index(True)))]
    elif check == [False,True,False]:
        score = (1 + min(num[0],num[2]))*max(num[0],num[2])
    elif check == [True,True,False] or check == [False,True,True]:
        score = 2*num[int(fabs(check.index(False)))]
    elif check == [True]*3:
        score = 3
    elif check == [True,False,True]:
        score = sum(num)
print score
