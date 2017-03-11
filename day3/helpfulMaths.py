a = raw_input()
a = a.split('+')
a = [int(x) for x in a]
a = sorted(a)
a = "+".join(str(x) for x in a)
print a
