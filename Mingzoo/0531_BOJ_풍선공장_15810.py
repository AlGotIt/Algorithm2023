N, M = map(int, input().split())
li = list(map(int, input().split()))

start, end = 0, max(li)*M
result = 0

while start <= end:
    m = (start+end)//2
    if sum([m//n for n in li]) >= M:
        result = m
        end = m-1
    else:
        start = m+1

print(result)
