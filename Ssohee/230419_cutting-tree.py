# https://www.acmicpc.net/problem/2805
# 백준 2805 나무자르기

n, m = map(int, input().split())
height = list(map(int, input().split()))

start, end = 1 , max(height)

while start <= end:
    result = 0
    mid = (start + end) // 2
    for h in height:
        if h - mid > 0:
            result += (h-mid)
    if result >= m:
        start = mid + 1
    else:
        end = mid -1
print(end)