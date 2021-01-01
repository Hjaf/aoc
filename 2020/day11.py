seatrows = list(open("day11input.txt", "r").read().split('\n'))
initial_seats = {} #true is taken

#create seat dictionary
y = 0
y_range = range(len(seatrows))
for row in seatrows:
    x_range = range(len(row))
    x = 0
    for seat in row:
        if seat != '.': # ignore floor
            initial_seats[(x, y)] = False
        x += 1
    y += 1

seats = dict(initial_seats)
def check_vacancy(seat, seats, los=False, vectors=[
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0), #(0, 0), # center
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1)
    ]):
    x = seat[0]
    y = seat[1]
    taken = 0
    for vector in vectors:
        adjacent = (x+vector[0], y+vector[1])
        if adjacent in seats:
            taken += int(seats[adjacent])
        elif los and x in x_range and y in y_range:
            taken += check_vacancy(adjacent, seats, los, [vector])
    else:
        return taken

def seating(keep_limit, los=False):
    seats_change = True
    while seats_change: #round_seats_state > seats_state:
        seats_change_count = len(seats)
        i_seats = dict(seats) #retain seating state
        for seat in seats:
            adjacent_taken_count = check_vacancy(seat, i_seats, los)  
            if seats[seat] and adjacent_taken_count >= keep_limit:
                seats_change_count += 1
                seats[seat] = False
            elif adjacent_taken_count == 0 and not seats[seat]:
                seats_change_count += 1
                seats[seat] = True
            else:
                seats_change_count -= 1
        seats_change = seats_change_count > 0

# part one
seating(4)
print(sum(seats.values()))
# part two
seats = dict(initial_seats)
seating(5, True)
print(sum(seats.values()))
