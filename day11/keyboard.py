dir = raw_input()
letters = raw_input()
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
if dir == "L":
    pos = +1
else:
    pos = -1
result = ""
for i in range(len(letters)):
    result += keyboard[keyboard.index(letters[i])+pos]
print result

