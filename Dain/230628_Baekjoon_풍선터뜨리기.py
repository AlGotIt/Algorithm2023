# python 3.9

from collections import deque

num = int(input())

q = deque(enumerate(map(int, input().split())))

result = []

while q:
    index, step = q.popleft()
    result.append(index + 1)

    if step > 0:
        q.rotate(-(step - 1))
    else:
        q.rotate(-step)

print(" ".join(map(str, result)))