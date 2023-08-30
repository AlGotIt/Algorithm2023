road = int(input()) # 길의 길이 
lights = int(input()) # 가로등 개수
light_loc = list(map(int, input().split())) # 가로등 위치
max_dis = light_loc[0]

for i in range(0, len(light_loc)-1):
    distance = light_loc[i+1] - light_loc[i]
    if distance % 2 == 0: distance //= 2
    else: distance = distance // 2 + 1

    if distance > max_dis:
        max_dis = distance

max_dis = max(max_dis, abs(road-light_loc[-1]))

print(max_dis)
