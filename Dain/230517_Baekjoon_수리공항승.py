# python 3.9

def solution(l_num, tape, leak):
    leak = sorted(leak)
    count = 1
    start = leak[0]
    for i in leak[1:]:
        if start <= i < start + tape:
            continue
        else:
            start = i
            count += 1
    return count

leak_num, tape = map(int, input().split())
leak = list(map(int, input().split()))

print(solution(leak_num, tape, leak))