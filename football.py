#to find whether the situation is dangerous or not(more than 7 players of a team are together or not)

def status(players):
    n = len(players)
    curr = players[0]
    i = 0
    while i < n-6:
        temp = 1
        while (players[i+1] == curr) and (temp <= 7) :
            temp += 1
            i += 1
        print temp
        if temp >= 7 :
            return "YES"
        i += 1
        curr = players[i]
        print temp
    return "NO"



players = raw_input()
print status(players) 
