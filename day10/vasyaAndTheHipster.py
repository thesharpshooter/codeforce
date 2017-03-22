temp = map(int,raw_input().split(" "))
min_sock = min(temp)
max_sock = max(temp)
print min_sock," ",(max_sock - min_sock)/2
