n = int(raw_input())
a = sorted(map(int,raw_input().split(" ")))
b = sorted(map(int,raw_input().split(" ")))
c = sorted(map(int,raw_input().split(" ")))
f1 = False
f2 = False
for i in range(n-1):
	if a[i] != b[i] :
		print a[i]
		f1 = True
		break
if f1 == False:
	print a[-1]
for j in range(n-2):
	if b[j] != c[j]:	
		print b[j]
		f2 = True
		break
if f2 == False:
	print b[-1]

