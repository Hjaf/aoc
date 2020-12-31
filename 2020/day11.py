seatrows = list(open("day11input.txt", "r").read().split('\n'))
occupied = 0
# - If a seat is empty(L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# - If a seat is occupied(  # ) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# - Otherwise, the seat's state does not change.
vacant_seats = {}
seat_count = 0
y = 0

for row in seatrows:
    x_max = len(row)
    x = 0
    for seat in row:
        if seat != '.': # ignore floor
            seat_count += 1
            vacant_seats[(x, y)] = (seat == 'L')
        x += 1
    y += 1

def check_vacancy(seat, seats):
    filled = 0
    x = seat[0]
    y = seat[1]
    adjacents = [
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
        (x-1, y),
        (x+1, y),
        (x-1, y+1),
        (x,y+1),
        (x+1, y+1)
    ]
    for adjacent in adjacents:
        if adjacent in vacant_seats and not seats[adjacent]:
            filled += 1
    return filled
filled_seats = 0


seat_change = seat_count
i = 0
# n = 30
# while n > i:
while seat_change != 0:
    round_seat_count = int(seat_count)
    seats = dict(vacant_seats)
    for seat in vacant_seats:
        free = vacant_seats[seat]
        taken_count = check_vacancy(seat, seats)
        if free and taken_count == 0:
            vacant_seats[seat] = False
            filled_seats += 1
            seat_count -= 1
        elif not free and taken_count >= 4:
            vacant_seats[seat] = True
            filled_seats -= 1
            seat_count += 1
    seat_change = seat_count - round_seat_count
    i += 1
print('filled seats: %s, available seats: %s' %(filled_seats, seat_count))