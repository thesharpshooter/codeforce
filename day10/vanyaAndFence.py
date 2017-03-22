temp = map(int,raw_input().split(" "))
height = map(int,raw_input().split(" "))
width = temp[0]
for x in height:
	if x >temp[1]:	
		width +=1 
print width
