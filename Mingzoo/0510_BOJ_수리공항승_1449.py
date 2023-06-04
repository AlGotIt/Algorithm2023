# 핀꽂기 문제와 유사
def pin(List, N, L, a):
    k = 0
    start = List[0][0]
    end = start+L
    for i in range(N):
        if (start < a[i] < end):
            continue
        else:
            start = List[i][0]
            end = start+L
            k += 1
    return k


N, L = map(int, input().split())
a = input().split(' ')
a.sort()

List = []
for i in range(N):
    myTuple = (int(a[i])-0.5, int(a[i])+0.5)
    List.append(myTuple)

# print(List)
print(pin(List, N, L, a))
