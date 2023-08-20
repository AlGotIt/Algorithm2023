# 백준 1411 비슷한 단어
# https://www.acmicpc.net/problem/1411

from itertools import combinations

# 한 단어가 몇개의 문자로 이뤄져있는지 같아야함 / 길이가 같아야함
def solution(w1, w2):
    ans = []
    for w in [w1, w2]:
        num = 0
        dic = dict()
        for i in w:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        ans.append(len(dic))

    if ans[0] == ans[1]:
        return True
    return False
            

n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

cnt = 0
for li in combinations(words, 2):
    if solution(li[0], li[1]):
        cnt +=1
print(cnt)

# n = 3
# words = ['abca', 'zbxz', 'opqr']

# cnt = 0
# if solution('abca', 'zbxz'):
#     cnt += 1

# print(cnt)