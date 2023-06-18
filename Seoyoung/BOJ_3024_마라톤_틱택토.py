n = int(input())

arr = [list(input()) for _ in range(n)]

find = False

def find_right(i,j):
    global find
    if(find == False):
        if(arr[i][j] != '.' and arr[i][j] == arr[i][j+1] and arr[i][j+1] == arr[i][j+2]):
            find = True
            print(arr[i][j])
            return

def find_down(i,j):
    global find
    if(find == False):
        if(arr[i][j] != '.' and arr[i][j] == arr[i+1][j] and arr[i+1][j] == arr[i+2][j]):
            find = True
            print(arr[i][j])
            return

def find_line(i,j):
    global find
    if(find == False):
        if(arr[i][j] != '.' and arr[i][j] == arr[i+1][j+1] and arr[i+1][j+1] == arr[i+2][j+2]):
            find = True
            print(arr[i][j])
            return

def find_line2(i,j):
    global find
    if(find == False):
        if(arr[i][j] != '.' and arr[i][j] == arr[i+1][j-1] and arr[i+1][j-1] == arr[i+2][j-2]):
            find = True
            print(arr[i][j])
            return

for i in range(n-2):
    for j in range(n-2):
        find_line(i, j)
for i in range(n-2):
    for j in range(2,n):
        print(i,j)
        find_line2(i,j)
for i in range(n):
    for j in range(n-2):
        find_right(i, j)
for i in range(n-2):
    for j in range(n):
        find_down(i, j)

if(find == False):
    print('ongoing')
