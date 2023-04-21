# n값 받기
n, m = map(int, input().split())

trees = list(map(int, input().split()))


def solution(start, end, trees):
    while start <= end:
        total = 0
        cut = (start+end)//2

        for tree in trees:
            if tree > cut:
                total += tree-cut
        if (total < m):
            end = cut - 1
        else:
            start = cut + 1
    return end


print(solution(1, max(trees), trees))

# def solution(n, m, trees):
#     cut = max(trees)
#     total = 0
#     while cut:
#         for i in range(n):
#             if (trees[i]-cut > 0):
#                 total += trees[i]-cut
#                 if (total == m):
#                     return cut
#         total = 0
#         cut -= 1
