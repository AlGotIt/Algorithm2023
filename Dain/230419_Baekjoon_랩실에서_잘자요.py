# python 3.9

"""
1. 바닥에는 M장의 논문이 있다.
2. 1부터 N까지 중복 가능한 페이지 번호는 빠진 게 있어서는 안된다.
3. 만약 빠진 것이 있다면 출력해야한다. 
4. 연속된 K장의 페이지 인쇄를 위해서는 5+2k 만큼의 잉크를 쓴다.
    - 잉크는 최대한 절약한다.
    - 잉크를 절약하기 위해서 존재하는 페이지를 또 뽑아도 된다.
"""

# 비용 비교 함수
def comparer(l1, l2):
    if len(l1) > 1:
        first = (l1[-1] - l1[0] + 1) * 2 + 5
    else: first = 7

    if len(l2) > 1:
        second = (l2[-1] - l2[0] + 1) * 2 + 5
    else: second = 7

    if first + second > (l2[-1] - l1[0] + 1) * 2 + 5:
        return True
    else:
        return False

# 1. 빠진 페이지 찾기
def ink_calculate(N , M ,pages):
    skipped_page = []
    page_num = 0

    for page_num in range(1, N + 1):
        if page_num not in pages:
            skipped_page.append(page_num)

    if not skipped_page: return 0

    # 2. 최소 잉크 가격 구하기
    #   - 거리가 가까운 것들끼리 구간을 나누어 묶는 것이 중요
    #   - 각 숫자들 사이의 거리를 구해서 구간 구분
    #   - 그룹화 한 것들의 최소비용 검증해서 합치기

    # 임시 그룹화(거리)
    group = [[skipped_page[0]]]
    g_idx = 0
    for i in range(1, len(skipped_page) - 1):
        left = skipped_page[i] - skipped_page[i-1]
        right = skipped_page[i+1] - skipped_page[i]

        if left <= right and left < 4:
            group[g_idx].append(skipped_page[i])
        else:
            group.append([skipped_page[i]])
            g_idx += 1
    group.append([skipped_page[-1]])

    # 그룹화한 것 검증(비용)
    i = 0
    while(len(group) > 1 and i < len(group) - 1):
        if comparer(group[i], group[i + 1]):
            group[i].extend(group[i + 1])
            del group[i + 1]
        else:
            i += 1
    
    # 총 비용
    ink = 0
    for l in group:
        if len(l) > 1:
            ink += 2 * (l[-1] - l[0] + 1) + 5
        else:
            ink += 7
    return ink


N, M = map(int, input().split())
pages = list(map(int, input().split()))

print(ink_calculate(N, M ,pages))