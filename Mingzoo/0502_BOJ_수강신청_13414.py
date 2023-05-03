import sys
# 시간제한 1초
input = sys.stdin.readline

# 딕셔너리


def solution():
    k, l = map(int, input().split())
    section = {}
    for number in range(l):  # 중복 key가 있다면 기존 값 제거
        section[input().rstrip()] = number

    # 순서 값에 맞게 정렬
    section = sorted(section.items(), key=lambda x: x[1])

    cnt = 0
    for stu_num in section:
        if cnt == k:
            break
        print(stu_num[0])
        cnt += 1


solution()
