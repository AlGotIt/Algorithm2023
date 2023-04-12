# dp

# n값 받기
n = int(input())

# 배열 값 받기
arr = list(map(int, input().split()))


def solution(arr):
    dp = []
    mini = arr[0]
    dp.append(0)
    for i in range(1, len(arr)):
        mini = min(arr[i], mini)
        dp.append(max(dp[i-1], arr[i]-mini))
    return dp


print(*solution(arr))
