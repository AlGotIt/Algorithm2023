w, h = map(int, input().split())
num_s = int(input())
stickers = []

for _ in range(num_s):
    sticker = list(map(int, input().split()))
    sticker.append(sticker[0] * sticker[1])
    stickers.append(sticker)

result = 0
for r in range(num_s):
    r1, c1, a1 = stickers[r]
    for c in range(r + 1, num_s):
        r2, c2, a2 = stickers[c]

        # 1. 둘 다 회전 안하고 붙이기
        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, a1 + a2)
        # 2. r만 회전하고 붙이기
        if (c1 + r2 <= h and max(c2, r1) <= w) or (max(c1, r2) <= h and c2 + r1 <= w):
            result = max(result, a1 + a2)
        # 3. c만 회전하고 붙이기
        if (r1 + c2 <= h and max(r2, c1) <= w) or (max(r1, c2) <= h and r2 + c1 <= w):
            result = max(result, a1 + a2)
        # 4. 둘 다 회전하고 붙이기
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, a1 + a2)

print(result)
