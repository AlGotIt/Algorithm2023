# 백준 13305 주유소
# https://www.acmicpc.net/problem/13305

n = int(input())

count = 1
distance = list(map(int, input().split()))
city_cost = list(map(int, input().split()))

cost = distance[0] * city_cost[0]
min_cost = city_cost[0]

while count < n - 1:
  if (min_cost <= city_cost[count]):
    cost += min_cost * distance[count]
  else:
    cost += city_cost[count] * distance[count]
    min_cost = city_cost[count]
  count += 1

print(cost)