gap_arr = []
bus_num, my_start = map(int, input().split())
for i in range(bus_num):
    start, gap, num = map(int, input().split())
    for i in range(num):
        if((start + (num * gap) >= my_start) and (start+(i*gap) >= my_start)):
            gap_arr.append((start+(i*gap)) - my_start)
if(len(gap_arr) == 0): print(-1)
else:  
    print(min(gap_arr))