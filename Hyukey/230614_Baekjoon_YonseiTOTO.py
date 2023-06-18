n, m = map(int, input().split())

min_mileages = []

for _ in range(n):
    p, l = map(int, input().split())
    mileages = sorted(list(map(int, input().split())), reverse=True)

    if p < l:
        min_mileages.append(1)
    else:
        min_mileages.append(mileages[l-1])

min_mileages.sort()
idx = 0
cnt = 0
while m > 0 and n > idx:
    m -= min_mileages[idx]
    if m >= 0:
        cnt += 1
    idx += 1

print(cnt)