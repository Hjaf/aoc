#import json # debugging
ifile = "day16input.txt"
ticket_data = list(open(ifile, 'r').read().split('\n\n'))

valid_ticket_values = {}
for ticket_value in ticket_data[0].splitlines():
    tva = ticket_value.split(': ')
    tvb = tva[1].split(' or ')
    tv_ranges = []
    for tv_range in tvb:
        tv_rgmm = tv_range.split('-') # tv_Ranges_Min_Max
        tv_ranges.extend(list(range(int(tv_rgmm[0]), int(tv_rgmm[1])+1)))
    valid_ticket_values[tva[0]] = tv_ranges

tickets = []
my_ticket = ticket_data[1].splitlines(False)[1].split(',')

for t in ticket_data[2].splitlines(False)[1:]: 
    tickets.append(t.split(','))
################################

def check_ticket_fields(ticket_fields):
    invalid = 0
    for field_value in ticket_fields:
        field_invalid = True
        for field_name in valid_ticket_values:
            if int(field_value) in valid_ticket_values[field_name]:
                field_invalid = False
        else: 
            if field_invalid:
                invalid = int(field_value)
    return invalid 

checked_tickets = {}
ticket_no = 0
for nearby_ticket in tickets:
    ticket_no += 1
    checked_tickets[ticket_no] = check_ticket_fields(nearby_ticket)

ans = 0
for ct in checked_tickets: 
    if checked_tickets[ct]:
        ans += checked_tickets[ct]

print('part one answer: %s\n-------' %(ans))

# print(json.dumps(checked_tickets, indent=4, sort_keys=False))
