# 230405 백준 2839 설탕배달

n = int(input())
cnt = 0

if n == 3 or n == 5:
    cnt = 1
if n == 4:
    cnt = -1
else: # n이 6이상
    rest = n % 5
    cnt = n // 5
    if rest == 0:   # 5로 나누어진다면
        print(cnt)
    else:   # 5로 안나누어진다면
        while cnt >= 0:
            if rest % 3 == 0:   #3으로 나누어지면
                cnt += rest // 3
                break
            else:   # 3으로 안 나뉘면
                rest += 5 
                cnt -= 1
        cnt = -1

print(cnt)          



# num = int(input())
# count = 0

# while num >= 0:
#   if num % 5 == 0:
#     count += int(num // 5)
#     print(count)
#     break
  
#   num -= 3
#   count += 1
  
# else:
#   print(-1)