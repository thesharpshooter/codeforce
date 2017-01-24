#Enter the weight of watermelon

weight = int(raw_input())
def inRange(weight):
    even = []
    i = 2
    while i <= weight :
        even.append(i)
        i += 2
    return even

def isSumEven(weight):
    even = inRange(weight)
    for x in even :
        if weight - x in even :
            return "YES"
    return "NO"

print isSumEven(weight)


