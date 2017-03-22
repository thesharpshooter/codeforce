temp = map(int,raw_input().split(" "))
total = sum(temp)
if total != 0 and total%5 == 0:
	print total/5 
else:
	print -1
