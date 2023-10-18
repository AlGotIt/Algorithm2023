# n, k = tuple(map(int, input().split()))
# arr = []
# cnt = 0
# kids = sorted(list(map(int, input().split())))
# ans = max(kids)


# def choose_number(curr_num):
#     global cnt, ans
#     if (curr_num == k and cnt == n):
#         temp = 0
#         temp_ans = 0
#         for elem in arr:
#             temp_ans += kids[elem+temp-1] - kids[temp]
#             temp += elem
#         ans = min(ans, temp_ans)

#     for i in range(1, n):
#         if (cnt+i > n):
#             return
#         arr.append(i)
#         cnt += i
#         choose_number(curr_num+1)
#         cnt -= i
#         arr.pop()


# choose_number(0)
# print(ans)


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

ans = []
for i in range(1, n):
    ans.append(kids[i] - kids[i-1])
ans.sort(reverse=True)

print(sum(ans[k-1:]))
