tickets = open('input/day5input.txt', 'r').readlines()
ticket_ids = {}

def highest_ticket_id(tickets):
    max_seat_id = 0
    for ticket in tickets:
        ticket_rows = list(range(128))
        ticket_seats = list(range(8))
        fields = list(ticket.strip())
        for field in fields:
            rmid = int(len(ticket_rows)/2) + int(len(ticket_rows)%2) # round int up, should be 128 rows.
            smid = int(len(ticket_seats)/2) + int(len(ticket_seats)%2) # round int up, should be 8 seats.
            if field == 'F':
                ticket_rows = ticket_rows[:rmid]
            elif field == 'B':
                ticket_rows = ticket_rows[rmid:]
            else: 
                ticket_row = ticket_rows[0]
            if field == 'L':
                ticket_seats = ticket_seats[:smid]
            elif field == 'R':
                ticket_seats = ticket_seats[smid:]
            if len(ticket_seats) == 1: # trigger on last iteration after range has been reduced.
                ticket_seat = ticket_seats[0]
        ticket_seat_id = ticket_row * 8 + ticket_seat
        ticket_ids[ticket_seat_id] = ticket.strip()
        max_seat_id = max(max_seat_id, ticket_seat_id)
    return max_seat_id

# part one
print('Part one answer: %s' %(highest_ticket_id(tickets)))

# part two
ticket_list = list(ticket_ids.keys())
ticket_list.sort()
for ticket_id in ticket_list:
    if ticket_id + 1 not in ticket_ids and ticket_id + 2 in ticket_ids:
        print('Part two answer: %s' %(ticket_id+1))