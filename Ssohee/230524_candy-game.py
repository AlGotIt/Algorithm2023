# 백준 3085 사탕게임
# https://www.acmicpc.net/problem/3085

def check():
    result = 1
    for j in range(n): #세로 최대 찾기
        maxi = 1
        for i in range(n-1):
            if candy[i][j] == candy[i+1][j]:
                maxi += 1
            else:
                maxi = 1    #초기화
            if maxi > result:
                result = maxi

    for i in range(n):  #가로 최대 찾기
        maxi = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                maxi += 1
            else:
                maxi = 1    #초기화
            if maxi > result:
                result = maxi
    return result

n = int(input())
candy = []
for i in range(n):
    candy.append(list(input()))

answer = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            answer = max(answer, check())
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i+1 < n:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            answer = max(answer, check())
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
print(answer)