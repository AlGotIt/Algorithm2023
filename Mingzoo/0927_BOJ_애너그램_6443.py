n = int(input())

arr = []


def print_num():
    for elem in arr:
        print(elem, end="")
    print()


def anagram(cnt):
    if (cnt == length):
        print_num()
        return

    # for j in range(length):
    #     arr.append(string[j])
    #     anagram(k+1)
    #     arr.pop()

    for k in visited:
        if visited[k]:
            visited[k] -= 1
            arr.append(k)
            anagram(cnt + 1)
            visited[k] += 1
            arr.pop()


for _ in range(n):
    string = sorted(list(input()))
    length = len(string)

    visited = {}

    for i in string:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    anagram(0)
