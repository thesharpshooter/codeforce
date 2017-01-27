def taxi(group):
  if sum(group)<=4 :
    return 1
  elif group[-1]==4:
    return 1 + taxi(group[:-1])
  elif (group[-1] + group[0] == 4):
    return 1 + taxi(group[1:-1])
  elif (group[-1] + group[0] > 4):
    return 1 + taxi(group[:-1])
  elif (group[-1] + group[0] + group[1])==4:
    return 1 + taxi(group[2:-1])
  elif (group[-1] + sum(group[:3]))==4:
    return 1 + taxi(group[3:-1])
n = int(input())
x = input().split()
x = [int(num) for num in x]
x.sort()
print (taxi(x))