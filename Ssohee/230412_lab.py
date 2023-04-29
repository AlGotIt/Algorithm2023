# 230405 백준 27446 랩실에서 잘자요
# https://www.acmicpc.net/problem/27446

# N, M = map(int, (input().split()))
# page_li = list(map(int, (input().split())))

# # N, M = 10, 8
# # page_li = [5, 7, 9, 10, 3, 4, 4, 3]

# total = [i for i in range(1, N+1)]  #전체 페이지
# page_li = list(set(page_li))    # 중복 제거
# page_li.sort()  #오름차순

# for p in page_li:
#     if p in total:
#         del total[total.index(p)]   # 빠진 페이지를 계산
    
total = [1, 4, 8, 11, 15]
#total = [1, 3, 5, 9]
#total = [1, 2, 6, 8]

# 4를 기준으로!!!
# 이제 total은 새롭게 출력해야할 페이지

gap = []
for i in range(len(total)-1):
    gap.append(total[i+1] - total[i])

new = []    # 4를 기준으로 나누기
result, start = 0, 0
for i in range(len(gap)):
    if gap[i] >= 4:
        new.append(total[start:i+1])
        start = i+1
new.append(total[start:])

print(new)

for n in new:
    result += 5 + 2*(n[-1]-n[0]+1)
        
print(result)
