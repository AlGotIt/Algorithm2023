N = int(input()) #골목길의 길이 N
road = input() #길이 N짜리 지도

a = road.count("EW") #"EW"가 있다면 무조건 선물을 놓아야 함
if road[0] == "W": #시작이 W라면 선물을 놓아야 함 - 움직일 수 없으므로 첫번째 칸에 선물이 있어야 함
    a += 1
if road[-1] == "E": #마찬가지로 마지막이 E라면 선물을 놓아야 함
    a += 1

print(a)