# python 3.9

# 해당 과목에 써야하는 최소 마일리지 구하기
def solution(P, L, miles):
    miles = sorted(miles, reverse=True)
    if P > L:
        m = miles[min(L-1, P-1)]
    else:
        m = 1
    if m > 36: m = 36
    return m

subject, mile = map(int, input().split())
needs = []

for s in range(subject):
    P, L = map(int, input().split())
    miles = list(map(int, input().split()))
    needs.append(solution(P, L, miles))

needs = sorted(needs)
count = 0
for n in needs:
    mile -= n
    if mile < 0: break
    count += 1

print(count)