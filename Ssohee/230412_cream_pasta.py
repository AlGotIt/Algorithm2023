# 230405 백준 25214 크림파스타
# https://www.acmicpc.net/problem/25214

N = int(input())
A = list(map(int, (input().split())))

result = [0] * N
m = A[0]
for i in range(1, N):
    m = min(m, A[i])
    result[i] = max(result[i-1], A[i] - m)
print(*result)


# 타임에러 #
# N = int(input())
# A = list(map(int, (input().split())))


# result = [0]
# for i in range(N):
#     M = result[-1]
#     for j in range(i):
#         x = A[i] - A[j] 
#         if x > M:
#             M = x
#     result.append(M)
    
# print(result[1:])