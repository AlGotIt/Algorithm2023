import sys
data = [] #처음 문자열을 읽어 저장할 배열
code_len = 0 #코드의 길이 2~8

def findNum(array): #입력된 숫자를 찾는 함수 정의
    if "".join(array) == "**** ** ** ****":
        return "0"
    elif "".join(array) == "  *  *  *  *  *":
        return "1"
    elif "".join(array) == "***  *****  ***":
        return "2"
    elif "".join(array) == "***  ****  ****":
        return "3"
    elif "".join(array) == "* ** ****  *  *":
        return "4"
    elif "".join(array) == "****  ***  ****":
        return "5"
    elif "".join(array) == "****  **** ****":
        return "6"
    elif "".join(array) == "***  *  *  *  *":
        return "7"
    elif "".join(array) == "**** ***** ****":
        return "8"
    elif "".join(array) == "**** ****  ****":
        return "9"
    else: #숫자에 해당하지 않으면 문자열 x 반환
        return "x"

for i in range(5): #5줄을 읽어 data 배열에 저장
    data.append(sys.stdin.readline())

code_len = len(data[0])//4 #코드의 길이: 입력된 문자열의 길이를 4로 나누어 구하기
code = "" #최종 코드를 저장할 문자열
number = [] #각각의 숫자를 임시로 저장할 배열

for j in range(code_len):
    for i in range(5):
        number.append(data[i][j*4:(j+1)*4-1]) #코드의 숫자별로 모으기
    code += findNum(number) #숫자 판별
    number= [] #배열 비우기
    if code[-1] == "x": #존재하지 않는 숫자인 경우 즉시 종료
        break

print(code)
try: #숫자가 아닌 경우: 문자열 x로 끝나기 때문에 int 변환 시 에러 발생
    code = int(code)
    if code % 2 == 0 and code % 3 == 0: #6의 배수인지 확인
        print("BEER!!")
    else:
        print("BOOM!!")
except:
    print("BOOM!!")