# to tell if the current situation is dangerous or not? 

def isDangerous(players):
    n = len(players)
    i = 0
    while i < n-1 :
        temp = 1
        curr = players[i]
        while i<n-1 and players[i+1] == curr and temp<=7 :
            temp += 1
            i += 1
        if temp >= 7 :
            return "YES"
        i += 1
    return "NO"

x = raw_input()
print isDangerous(x)

        
