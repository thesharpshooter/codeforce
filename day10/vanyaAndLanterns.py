temp = map(int,raw_input().split(" "))
a = map(int,raw_input().split(" "))
if len(a) == 1 :
	print float(max(a[0]-0,temp[1]-a[0]))
else:
	a = sorted(a)
	min_dis = max([(a[i+1]-a[i]) for i in range(temp[0]-1)])
	min_dis2 = max((a[0]-0),temp[1]-a[-1])
	if min_dis2 > min_dis/2 :
		print float(min_dis2)
	else:
		print float(min_dis)/2
