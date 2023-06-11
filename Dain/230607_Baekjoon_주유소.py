# python 3.9

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
min_price = price[0]
for i in range(n-1):
    if min_price > price[i]: min_price = price[i]
    total += min_price * road[i]
        
print(total)