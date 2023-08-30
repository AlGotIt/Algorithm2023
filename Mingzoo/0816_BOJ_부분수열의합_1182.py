from itertools import combinations

n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

cnt = 0

for i in range(1, n+1):
    comb = combinations(arr, i)
    for j in list(comb):
        if sum(j) == s:
            cnt += 1
print(cnt)
