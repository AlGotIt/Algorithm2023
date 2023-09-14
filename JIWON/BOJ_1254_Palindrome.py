import sys
S = sys.stdin.readline().strip() #입력받기

def palindrome(string):
    for i in range(len(S)):
        if string[i:] == string[i:][::-1]: #문자열의 시작을 뒤로 보내면서 해당하는 부분이 palindrome인지 확인
            break #맞다면 반복문 종료
    return len(S)+i #palindrome인 부분을 제외한 앞부분의 길이를 더함

p = palindrome(S) #p는 palindrome이 되기 위한 문자열의 길이
print(p)