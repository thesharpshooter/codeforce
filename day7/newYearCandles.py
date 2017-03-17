temp = map(int,raw_input().split(" "))
a = temp[0]
b = temp[1]
hrs = a
while a/b >=1 :
    hrs += a/b
    a = a/b + a%b
print hrs
