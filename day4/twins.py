n = int(raw_input())
coins = map(int,list(raw_input().split(" ")))
coins = sorted(coins)
def count_coins(coins):
    if n == 1:
        return 1
    my_coins = 0
    my_sum = 0
    for i in range(n):
        my_sum += coins[n-1-i]
        my_coins += 1
        if my_sum > sum(coins[:(n-i-1)]):
            return my_coins
print count_coins(coins)
