# python 3.9

# 입력 시간 단축
import sys
input=sys.stdin.readline

avail, student = map(int, input().split())
line = dict()

# 학번 = key, 순서 = value
for i in range(student):
    line[input().rstrip()] = i

# value를 기준으로 정렬
line = sorted(line.items(), key= lambda x : x[1])

for i in range(min(avail, len(line))):
    print(line[i][0])
