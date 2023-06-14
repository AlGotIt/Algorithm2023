# 그리디
# 실패한 풀이
# 10분 청소시간 고려 안함
# def solution(book_time):
#     k = 0
#     reserved = []
#     # print(book_time.sort(key=lambda x:x[1])) 이건 안됨
#     # [['14:20', '15:20'], ['15:00', '17:00'], ['16:40', '18:20'], ['14:10', '19:20'], ['18:20', '21:20']]
#     #끝내는 시점이 빠른 순으로 정렬
#     book_time.sort(key=lambda x:x[1])
#     for i in range(len(book_time)):
#         if (book_time[i][0] > book_time[k][1]):
#             print(i)
#             reserved.append(i)
#             print(reserved)
#     return len(reserved)+1


# 알고 스터디 끝난 후 다시 푼 풀이
# 분으로 시간 바꿔줌
def toMin(time):
    hour, min = time.split(':')
    return int(hour)*60 + int(min)


def solution(book_time):
    arr = []
    for start, end in book_time:
        start_time = toMin(start)
        end_time = toMin(end) + 10  # 청소시간 10분 추가
        arr.append((start_time, 'start'))
        arr.append((end_time, 'end'))
    # 입실시간기준으로 정렬
    arr.sort()
    # print(arr)
    # endTime = []
    # room = 0
    # for time in arr:
    #     if(time[0] < endTime[0]):
    #         endTime.append(time[1])
    #     endTime.sort()

    # 여기서부터 다른 풀이
    # 연달아 start가 나오게되면 방이 계속 필요하다/해당 연산의 최대가 필요한 방의개수가 됨
    room = 0
    max_room = 0
    for s, e in arr:
        if (e == 'start'):
            room += 1
        else:
            room -= 1
        if (max_room < room):
            max_room = room
    return max_room
