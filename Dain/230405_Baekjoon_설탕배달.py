sugar = int(input())
answer = 0

while sugar >= 0:
    if sugar % 5 == 0:
        print(answer + sugar // 5)
        break
    sugar -= 3
    answer += 1
if sugar < 0:
    print(-1)