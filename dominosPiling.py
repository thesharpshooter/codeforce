#Calculate maximum no of dominos(2*1) that can be put to cover the rectangular box of given dimension

m, n = map(int, raw_input().split(" "))
area = m*n
if (area % 2 == 0):
    print area/2
else:
    print (area-1)/2
