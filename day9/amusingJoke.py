a = raw_input()
b = raw_input()
mix = list(raw_input())
before = list(a + b)
set_before = list(set(before))
set_after = list(set(list(mix)))
tuple_before = []
tuple_after = []
for x in set_before:
    tuple_before.append((x,before.count(x)))
for y in set_after:
    tuple_after.append((y,mix.count(y)))
if tuple_before == tuple_after:
    print "YES"
else:
    print "NO"
