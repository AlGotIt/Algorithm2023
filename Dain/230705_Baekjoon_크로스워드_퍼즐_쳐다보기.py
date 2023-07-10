R, C = map(int, input().split())
puzzle = []
for i in range(R):
    puzzle.append(list(input()))

d = []

# 가로 단어
c = 0
for r in range(R):
    word = puzzle[r][0]
    for c in range(C-1):
        if word == "#": word = ''
        now = puzzle[r][c+1]
        if now != "#": word += now
        else:
            if len(word) > 1: d.append(word)   
            word = ''
    if len(word) > 1:
        d.append(word)

# 세로 단어     
c = 0
for c in range(C):
    word = puzzle[0][c]
    for r in range(R-1):
        if word == "#": word = ''
        now = puzzle[r+1][c]
        if now != "#": word += now
        else:
            if len(word) > 1: d.append(word)   
            word = ''
    if len(word) > 1: d.append(word)

print(sorted(d)[0])