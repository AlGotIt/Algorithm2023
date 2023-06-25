# 백준 12018 연세 토토
# https://www.acmicpc.net/problem/12018

n, m = map(int,input().split())

cnt = 0
result=[]

for i in range(n):
  p, l = map(int,input().split())
  mile = list(map(int,input().split()))
  mile.sort()
  if p < l:
    result.append(1)
  else:
    result.append(mile[l-1])

result.sort()
for i in result:
      if m - i >= 0:
        m -= i
        cnt += 1
      else:
         break
print(cnt)