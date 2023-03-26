def solution(N, number):
    if N == number:
        return 1

    s = [set() for _ in range(8)]

    for i, v in enumerate(s, start=1):
        v.add(int(str(N)*i))

    for i in range(1, 8):
        for j in range(i):
            for n1 in s[j]:
                for n2 in s[i-j-1]:
                    s[i].add(n1+n2)
                    s[i].add(n1-n2)
                    s[i].add(n1*n2)
                    if n2 != 0:
                        s[i].add(n1//n2)
        
        if number in s[i]:
            answer = i+1
            break
    else:
        answer = -1
    
    return answer

N = 5
number = 12
print(solution(N, number))