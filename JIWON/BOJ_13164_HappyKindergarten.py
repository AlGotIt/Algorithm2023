import sys
N, K = map(int, sys.stdin.readline().split())
kids = list(map(int, sys.stdin.readline().split()))

dif = []

for i in range(1,len(kids)):
    dif.append(kids[i]-kids[i-1])

dif.sort(reverse=True)
tshirt = sum(dif[K-1:])
print(tshirt)