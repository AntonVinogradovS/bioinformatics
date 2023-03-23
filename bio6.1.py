money = int(input())
Coins = [int(x) for x in input().split(",")]
MinNumCoins = {}
MinNumCoins[0] = 0
for m in range(1, money + 1):
    MinNumCoins[m] = money**2
    for i in Coins:
        if m >= i:
            if MinNumCoins[m - i] + 1 < MinNumCoins[m]:
                MinNumCoins[m] = MinNumCoins[m - i] + 1
print(MinNumCoins[money])