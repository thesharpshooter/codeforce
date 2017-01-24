m,n,a = map(int,raw_input().split(" "))
#a = int(raw_input("Enter the size of the square"))

def squares(length, width, square):
    nl = 0
    nw = 0
    if length % square == 0:
        nl = length//square 
    else:
        nl = length//square + 1
    if width % square == 0:
        nw = width//square
    else:
        nw = width//square + 1
    return nl*nw
print squares(m, n, a)


