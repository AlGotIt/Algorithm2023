# 백준 20126 교수님의 기말고사
# https://www.acmicpc.net/problem/20126

n, m, s = map(int, input().split())

time = []
for i in range(n):
    x, y = map(int, input().split())
    time.append([x, x+y])
time.sort(key = lambda x : x[0])

def case1():    #시험 중간에 가능한지
    for i in range(n-1):
        if time[i+1][0]- time[i][1] >= m:
            return time[i][1]

def case2():    #모든 시험이 끝나고 가능한지
    if s - time[-1][1] >= m:
        return time[-1][1]

if time[0][0] >= m: #시험 시작하기 전에 가능한지
    print(0)
elif case1() != None:
    print(case1())
elif case2() != None:
    print(case2())
else:
    print(-1)  