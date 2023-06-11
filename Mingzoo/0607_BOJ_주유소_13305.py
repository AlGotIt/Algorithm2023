n = int(input())
ans = 0
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = prices[0]

for i in range(n-1):  # 마지막 가격 무필요
    if (min_price > prices[i]):
        min_price = prices[i]

    ans += min_price * distances[i]

print(ans)
