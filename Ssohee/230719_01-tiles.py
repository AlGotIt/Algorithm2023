# https://www.acmicpc.net/problem/1904
# 백준 1904 01타일

def fibo(n):
    if n == 0 or n == 1:
        return 1
    return n * fibo(n-1)

def solution(n):
    result = 0
    num = n//2 + 1 
    for i in range(num):
        zero_n = i
        one_n = n - i*2
        result += fibo(zero_n + one_n) // (fibo(zero_n) * fibo(one_n))
    return result

n = int(input())
print(solution(n)%15746)

###################################################

dp = [0] * 100000
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])

#길이 n-2인 수열 뒤에 00 추가 (dp[i-2]) + 길이 n-1인 수열 뒤에 1 추가(dp[i-1])