# https://www.acmicpc.net/problem/1182
# 백준 1182 부분수열의 합

N, S = map(int, input().split())
li = list(map(int, input().split()))
result = 0

def com(arr, n):
    li = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        for rest in com(arr[i+1:], n-1):
            li.append([arr[i]]+rest)
    return li

        
for i in range(1, N+1):
    new_li = com(li, i)
    for new in new_li:
        if sum(new) == S:
            result += 1
print(result)
