"""
4개 칸에서 1개

5개 칸에서 2개 
-> 4개 칸에서 1개  + 3개 칸에서 1개 + 2개 칸에서 1개 + 1개 칸에서 1개

6개 칸에서 3개 
-> 5개 칸에서 2개(4개 칸에서 1개  + 3개 칸에서 1개 + 2개 칸에서 1개 + 1개 칸에서 1개) = 10
   + 4개 칸에서 2개(3개 칸에서 1개 + 2개 칸에서 1개 + 1개 칸에서 1개) = 6
   + 3개 칸에서 2개(2개 칸에서 1개 + 1개 칸에서 1개) = 3
   + 2개 칸에서 2개(1개 칸에서 1개) = 1

7개 칸에서 4개
 = 6개 칸에서 3개 = 20
 + 5개 칸에서 3개(4개 칸에서 2개 + 3개 칸에서 2개 + 2개 칸에서 2개)
 + 4개 칸에서 3개(3개 칸에서 2개 + 2개 칸에서 2개)
 + 3개 칸에서 3개(2개 칸에서 2개)
"""
testcase = int(input())
for t in range(testcase):
    N, M = map(int, input().split())
    result = 1
    divi = 1
    for i in range(N):
        result *= (M - i)
        divi *= (N - i)
    if N < 2:
        print(result) 
    else:
        print(result//divi)
        
        
