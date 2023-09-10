n = int(input())
expected = []
for _ in range(n):
    expected.append(int(input()))

# 정렬
expected.sort()

dissatisfaction = 0
# print(expected)

for i in range(n):
    if (expected[i] < i+1):
        dissatisfaction += abs(i+1-expected[i])

print(dissatisfaction)
