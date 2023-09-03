n = int(input())
m = int(input())
arr = list(map(int, input().split()))

if m == 1:
    print(max(arr[0], n-arr[0]))
else:
    arr_gap = -1
    # 가로등 사이의 최대간격
    for i in range(1, m):
        arr_gap = max(arr_gap, arr[i]-arr[i-1])
    if(arr_gap%2 == 0):
        arr_gap = arr_gap//2
    else:
        arr_gap = arr_gap//2 + 1
    # 가로등 맨 앞,뒤로의 최대간격    
    gap = max(arr[0], n-arr[-1])
    # 둘 중 최댓값 출력
    print(max(arr_gap, gap))
    

# 시간초과 코드;;; 

# add = 1
# a = False
# result = 0
# if m == 1:
#     result = max(arr[0], n-arr[0])
# else:
#     while 1:
#         for i in range(m-1):
#             if(arr[i] - add) > 0: 
#                 a = False
#                 break
#             if(arr[i+1] - add > arr[i] + add):
#                 a = False
#                 break
#             else:
#                 a = True
#                 continue
#         if a == True:
#             result = add
#             break
#         add += 1
# print(result)
