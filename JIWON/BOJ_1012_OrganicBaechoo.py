import sys
sys.setrecursionlimit(10000) #최대 재귀 깊이값 조정

def DFS(x,y): #DFS 함수 정의 
    global M,N #M,N 값은 전역 변수
    if x>=M or x<=-1 or y>=N or y<=-1: #범위에서 벗어나면
        return False #종료
    if baechoo[y][x] == 1 and visited[y][x] == False: #해당 위치에 배추가 있고 아직 방문하지 않은 상태라면
        visited[y][x] = True #방문 기록 후 인접 노드들에 대해 모두 DFS 수행
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)
        return True
    else: #해당 위치에 배추가 없거나 이미 방문했다면 종료
        return False
    
def test(): #테스트케이스 수에 따라 각각 수행될 함수
    global M,N #전역 변수로 이용할 배추밭의 크기 M*N
    M, N, K = map(int, sys.stdin.readline().split()) #배추 밭의 크기 M*N와 배추의 개수 K도 함께 입력받음.
    global baechoo #배추 위치를 저장할 이중 배열. (x,y) 위치에 배추가 있다면, baechoo[y][x]가 배추의 위치이다.
    global visited #해당 배추를 방문했는지 확인할 배열. True/False로 기록될 것임.
    global cnt #배추 블록의 개수를 저장할 전역 변수

    baechoo = [[0]*M for i in range(N)]
    visited = [[False]*M for i in range(N)]

    for i in range(K):
        X,Y = map(int,sys.stdin.readline().split())
        baechoo[Y][X] = 1 #해당 위치에 배추가 있다는 표시

    for j in range(N):
        for i in range(M):
            if baechoo[j][i] == 1 and visited[j][i] == False: #배추가 있고 방문하지 않았다면
                DFS(i,j) #DFS 수행
                cnt += 1 #해당 블록의 개수 1개 추가

T = int(sys.stdin.readline()) #테스트 케이스의 수를 가장 먼저 입력 받음.
for i in range(T):
    cnt = 0 #각 테스트 케이스에 대해 cnt의 개수 0으로 초기화
    test() #test 함수를 수행
    print(cnt) #최종 배추흰지렁이 수 출력