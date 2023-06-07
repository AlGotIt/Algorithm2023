n = input()
dist = list(map(int, input().split()))
arr = list(map(int, input().split()))

m = arr[0]
result = 0
for i in range(len(arr)-1):
    m = arr[i] if arr[i] <= m else m
    result += m * dist[i]
print(result)