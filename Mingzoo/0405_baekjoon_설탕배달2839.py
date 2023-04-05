# 5의 배수

# def divide(N):
#     sugar = N // 5
#     remaining_sugar = N % 5
#     if (remaining_sugar == 0):
#         return sugar
#     if (remaining_sugar >= 3):
#         sugar = sugar + (remaining_sugar // 3)
#         return sugar
#     else:
#         return -1

# def solution(N):
#     if (N == 4):
#         return -1
#     else:
#         if N % 5 == 0:
#             return N // 5
#         elif N % 3 == 0:
#             return N // 3
#         else:
#             sugar = N // 5
#             return sugar + (sugar // 3)

def solution(N):
    sugar = 0
    while N >= 0:
        if N % 5 == 0:
            sugar += N // 5
            return sugar

        N -= 3
        sugar += 1

    else:
        return -1


N = int(input())
print(solution(N))
