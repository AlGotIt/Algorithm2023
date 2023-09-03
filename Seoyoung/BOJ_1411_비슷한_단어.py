n = int(input())
arr = [list(input()) for _ in range(n)]
result = 0

origin_match_arr = []
compare_match_arr = []

while len(arr) > 1:
    for i in range(len(arr) - 1):
        isMatch = True
        for j in range(len(arr[0])):  
            find = arr[0][j] in origin_match_arr  # 원본 배열에 a 가 잇는지
            if find:  # 잇으면
                index = origin_match_arr.index(arr[0][j])  # 인덱스 찾아서
                match = compare_match_arr[index]  # 비교 배열에서 찾기 x
                if arr[i+1][j] != match:
                    isMatch = False
                    break
            else:
                if arr[i+1][j] not in compare_match_arr:
                    origin_match_arr.append(arr[0][j])  # [a]
                    compare_match_arr.append(arr[i+1][j])  # [x]
                else:
                    isMatch = False
                    break
        if isMatch:
            result += 1
                
        origin_match_arr = []
        compare_match_arr = []

    arr.pop(0)

print(result)

