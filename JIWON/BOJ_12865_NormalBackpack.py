import sys

N, K = map(int,sys.stdin.readline().split())
WV = [(0,0)]
dp = [[0]*(K+1) for i in range(N+1)] #dp 생성

for i in range(N):
    W, V = map(int,sys.stdin.readline().split())
    WV.append((W,V)) #WV[i][0]이 weight, WV[i][1]이 value값을 가짐


for i in range(1,N+1):
    w = WV[i][0]
    v = WV[i][1]
    for j in range(1,K+1):
        if j < w :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])

print(dp[N][K])