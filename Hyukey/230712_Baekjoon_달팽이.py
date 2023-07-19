N = int(input())
num = int(input())

board = [[0] * N for _ in range(N)]

movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cur_num = 1
step = 0
cur_row, cur_col = N//2, N//2

board[cur_row][cur_col] = cur_num
ans_row, ans_col = cur_row, cur_col

while cur_num < N**2:
    cur_row -= 1
    cur_col -= 1
    step += 2

    for d_row, d_col in movement:
        for _ in range(step):
            cur_num += 1
            cur_row += d_row
            cur_col += d_col
            board[cur_row][cur_col] = cur_num
            if cur_num == num:
                ans_row, ans_col = cur_row, cur_col

for row in board:
    print(" ".join(map(str, row)))
print(ans_row+1, ans_col+1)