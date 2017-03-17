wrd = raw_input()
wrd = wrd.replace("WUB"," ")
temp = wrd.split(" ")
string = []
for x in temp:
    if x != "":
        string.append(x)
print " ".join(string)
