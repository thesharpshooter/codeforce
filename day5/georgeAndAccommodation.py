rooms = int(raw_input())
count = 0
for i in range(rooms):
    room = map(int,raw_input().split(" "))
    if (room[1]-room[0]) >= 2:
        count += 1
print count
