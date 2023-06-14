def solution(a, edges):
    if sum(a) != 0:
        return -1
    else:
        tree = [[] for _ in range(len(a))]

        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

    return answer