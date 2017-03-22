temp = map(int,raw_input().split(" "))
a = map(int,raw_input().split(" "))
x = sum(map(lambda z : z<=5-temp[1],a))
print x/3

