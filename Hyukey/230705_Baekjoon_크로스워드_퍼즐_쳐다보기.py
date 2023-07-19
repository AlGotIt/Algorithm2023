R, C = map(int, input().split())

puzzle = [list(input()) for _ in range(R)]
dic = []


for i in range(R):
    col = 0
    word = ''
    while col < C:
        if puzzle[i][col] != '#':
            word += puzzle[i][col]
        else:
            if len(word) > 1:
                dic.append(word)
            word = ''
        col += 1
    if len(word) > 1:
        dic.append(word)

for j in range(C):
    row = 0
    word = ''
    while row < R:
        if puzzle[row][j] != '#':
            word += puzzle[row][j]
        else:
            if len(word) > 1:
                dic.append(word)
            word = ''
        row += 1
    if len(word) > 1:
        dic.append(word)

dic.sort()
print(dic[0])