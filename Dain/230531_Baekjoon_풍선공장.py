N, M = map(int, input().split())
eff = list(map(int, input().split()))

# 최대 시간 = 가장 오래 걸리는 스태프가 모든 풍선을 다 만들 때
min, max = 0, max(eff)*M 
time = 0
while min <= max:
    # 절반 시간
    mid = (min+max)//2 
    # m만큼의 시간 안에 만들 수 있는 최대 풍선 개수 >= 풍선 개수
    a = sum([mid//n for n in eff])
    # 요구 풍선 개수 이상
    if a >= M:
        # 시간 갱신
        time = mid
        # 최대 시간 -> mid - 1
        max = mid - 1
    # 요구 풍선 개수 이하
    else:
        # 최소 시간 -> mid + 1
        min = mid + 1
print(time)