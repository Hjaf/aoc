import json
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
ticket = ticket_data[1].splitlines(False)[1].split(',')

for t in ticket_data[2].splitlines(False)[1:]: 
    tickets.append(t.split(','))

checked_tickets = {}
ticket_no = 0
for nearby_ticket in tickets:
    ticket_no += 1
    invalid_field_val = 0
    for ticket_field in nearby_ticket:
        ticket_field_invalid = True
        ticket_fields = {}
        for ticket_field_name in valid_ticket_values:
            if int(ticket_field) in valid_ticket_values[ticket_field_name]:
                ticket_fields[ticket_field_name] = int(ticket_field)
                ticket_field_invalid = False 
        else: 
            if ticket_field_invalid: 
                invalid_field_val = int(ticket_field)
    ticket_fields['invalid'] = invalid_field_val
    checked_tickets[ticket_no] = ticket_fields
ans = 0
for checked_ticket in checked_tickets: 
    ans += int(checked_tickets[checked_ticket].get('invalid'))

#print(json.dumps(checked_tickets, sort_keys=True, indent=4))
print(ans)
