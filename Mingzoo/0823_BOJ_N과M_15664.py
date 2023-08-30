from itertools import combinations

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

comb = combinations(arr, m)

comb = sorted(list(set(comb)))

for elem in comb:
    print(*elem)
