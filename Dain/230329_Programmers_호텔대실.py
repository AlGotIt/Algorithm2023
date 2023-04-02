def solution(book_time):
    answer = [1]
    book_time.sort(key=lambda x:x[0])

    for b in range(len(book_time)):
        s, e = book_time[b]
        s = s.split(':')
        s = int(s[0]) * 60 + int(s[1])
        e = e.split(':')
        e = int(e[0]) * 60 + int(e[1]) + 10
        book_time[b] = [s, e]
    print(book_time)

    count = 0
    s, e = book_time[0][0], book_time[0][1]
    for i in range(0, len(book_time)):
        if len(book_time[i]) == 3: continue

        count += 1
        book_time[i].append(True)
        end = book_time[i][1]
        
        j = i + 1
        while j < len(book_time):
            if book_time[j][0] >= end and len(book_time[j]) < 3:
                book_time[j].append(True)
                end = book_time[j][1]
            j += 1
    return count

b = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# b = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
# b = [["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]
print(solution(b))