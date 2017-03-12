instruction = raw_input()
commands = ['H','Q','9']
def inst(word):
    for x in word :
        if x in commands:
            return 'YES'
    return 'NO'
print inst(instruction)
