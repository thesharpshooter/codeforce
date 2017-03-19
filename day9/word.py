string = raw_input()
lower_count = sum(map(str.islower,string))
upper_count  = sum(map(str.isupper,string))
if lower_count < upper_count:
    print string.upper()
else:
    print string.lower()
