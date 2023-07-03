N = int(input())
balloons = list(map(int, input().split()))
balloons_idx = [(i+1, balloons[i]) for i in range(N)]

answer = []

cur_index = 0
while True:
    idx, step = balloons_idx.pop(cur_index)
    answer.append(idx)
    N -= 1
    if N == 0:
        break
    if step > 0:
        step -= 1
    cur_index = cur_index + step
    cur_index %= N
    if cur_index < 0:
        cur_index += N
    if cur_index >= N:
        cur_index -= N

print(" ".join(map(str,answer)))