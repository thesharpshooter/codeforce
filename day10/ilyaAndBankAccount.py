amount = raw_input()
if int(amount) >= 0:
	print amount
else:
	temp1 = amount[:-1]
	temp2 = amount[:-2]+amount[-1]
	if int(temp1) < int(temp2):
		print int(temp2)
	else:
		print int(temp1)
