stones = int(raw_input())
colors = raw_input()

def calculate(colors):
    n = len(colors)
    if n <=1:
        return 0
    a = colors
    curr = a[0]
    nex = a[1]
    if curr == nex:
        return 1 + calculate(a[1:])
    return calculate(a[1:])
print calculate(colors)

