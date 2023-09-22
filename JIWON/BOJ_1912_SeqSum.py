n = int(input()) #n개의 정수
numbers = list(map(int,input().split())) #정수의 수열을 입력받아 정수형으로 변환하여 numbers라는 배열에 저장

dp = [numbers[i] for i in range(n)] #각 구간에서의 최대합을 저장할 배열 dp. i번째 숫자를 저장해놓음.

for i in range(1,n): #i=1일때부터
    if numbers[i] > dp[i-1]+numbers[i]: #i번째 수+앞에서부터의 합과 해당 위치의 숫자 중 큰 값을 선택하여 저장
        dp[i] = numbers[i]
    else:
        dp[i] = dp[i-1]+numbers[i]

print(max(dp)) #dp배열에서의 최대 숫자=최대합