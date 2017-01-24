# Change strings that are too long (n > 10)

n = int(raw_input())
words = []
while n > 0:
    word = raw_input()
    words.append(word)
    n -= 1

for x in words :
    if len(x) >10 :
        print x[0]+str(len(x)-2)+x[-1]
    else:
        print x

