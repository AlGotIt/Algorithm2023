# 230405 백준 2839 설탕배달
# https://www.acmicpc.net/problem/2839

n = int(input())
cnt = 0

if n == 3 or n == 5:
    cnt = 1
if n == 4:
    cnt = -1
else: # n이 6이상
    rest = n % 5
    cnt = n // 5
    if rest != 0:   # 5로 안나누어지면
        while cnt >= 0: 
            if rest % 3 == 0:   # 3으로 나누어지면
                cnt += rest // 3    # 3의 몫만큼 cnt추가
                break
            else:   # 3으로 안 나뉘면
                rest += 5 
                cnt -= 1
if cnt > 0 :
    print(cnt)
else:
    print(-1)          
