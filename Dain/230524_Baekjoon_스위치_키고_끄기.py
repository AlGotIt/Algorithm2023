def boy_control(switch, num):
    n = num
    i = 2
    while n < len(switch):
        switch[n] = 1 if switch[n] == 0 else 0
        n = num * i
        i += 1
    return switch

def girl_control(switch, num):
    pos = 0
    while num - pos > 0 and num + pos < len(switch):
        if pos == 0:
            switch[num] = 1 if switch[num] == 0 else 0
        elif switch[num - pos] == switch[num + pos]:
            switch[num - pos] = 1 if switch[num - pos] == 0 else 0
            switch[num + pos] = 1 if switch[num + pos] == 0 else 0
        else:
            break
        pos += 1
    return switch

s_num = int(input())
switches = [0]
switches.extend(list(map(int, input().split())))
students_num = int(input())

for _ in range(students_num):
    sex, num = map(int, input().split())
    if sex == 1:
        switches = boy_control(switches, num)
    else:
        switches = girl_control(switches, num)

for s in range(1, len(switches)): 
    if s % 20 == 0:
        print(switches[s])
    else: print(switches[s], end=' ')