temp = map(int,raw_input().split(" "))
pix = []
for i in range(temp[0]):
	curr = raw_input().split(" ")
	pix += curr
if set(pix) <= set(["W",'G','B']):
	print "#Black&White"
else:
	print "#Color"
