# perform operations in bit language (BIT ++ )

def value(operand):
    if operand == "X++" or operand == "++X":
        return 1
    else :
        return -1



num = int(raw_input())
x = 0
while (num > 0):
    statement = raw_input()
    x = x + value(statement)
    num -= 1
print x

