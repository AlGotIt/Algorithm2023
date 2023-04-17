# 230405 백준 27446 랩실에서 잘자요
# https://www.acmicpc.net/problem/27446

# N, M = map(int, (input().split()))
# page_li = list(map(int, (input().split())))

N, M = 10, 8
page_li = [5, 7, 9, 10, 3, 4, 4, 3]

total = [i for i in range(1, N+1)]  #전체 페이지
page_li = list(set(page_li))    # 중복 제거
page_li.sort()  #오름차순

for p in page_li:
    if p in total:
        del total[total.index(p)]   # 빠진 페이지를 계산
    
#이제 total은 새롭게 출력해야할 페이지
term = 
for i in range(len(total)):
