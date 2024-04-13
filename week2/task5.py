def find(spaces, stat, n):
    seat_count = []
    space_available = False
    found_index = None
    min_seat_count = float('inf')
    count = range(int(len(spaces)))
    
    for x in count:
        seat_count.append(spaces[x] - n)
        if stat[x] == 1:
            if seat_count[x] == 0:
                found_index = x
                space_available = True
                break
            elif seat_count[x] > 0 and seat_count[x] < min_seat_count:
                found_index = x
                min_seat_count = seat_count[x]
                space_available = True

    if space_available:
        return print(found_index)
    else:
        return print(-1)



find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2


