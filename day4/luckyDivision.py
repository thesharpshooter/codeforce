num = raw_input()
lucky_numbers = ['4','7']
def is_lucky1(number):
    for x in number:
        if x not in lucky_numbers:
            return False
    return True

def divisor(num):
    for x in range(1,num+1):
        if num%x == 0 and is_lucky1(str(x)):
            return True
    return False
result = is_lucky1(num) or divisor(int(num))
if result:
    print 'YES'
else:
    print 'NO'

