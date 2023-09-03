n = int(input())

for i in range(n):
    n, m = map(int, input().split())

    dp = [[0]*m for _ in range(n)]

    for i in range(n-1, m): 
        dp[n-1][i] = 1

    for i in range(n-2, -1, -1):
        for j in range(i+(m-n), i-1, -1):
            dp[i][j] = dp[i][j+1] + dp[i+1][j+1]

    print(sum(dp[0]))


