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
ticket_field_positions = []
ticket_no = 0
for nearby_ticket in tickets:
    ticket_no += 1
    invalid_field_val = 0
    i = 0
    for ticket_field_value in nearby_ticket:
        i += 1
        # print('iter %s, field %s' %(i, ticket_field))
        ticket_field_invalid = True
        ticket_field_names = []
        ticket_fields = {}
        # ticket_fields
        for ticket_field_name in valid_ticket_values:
            # print('field name: %s - field no: %s, field value: %s' %
                #   (ticket_field_name, i, ticket_field_value))
            if int(ticket_field_value) in valid_ticket_values[ticket_field_name]:
                ticket_field_positions.append([ticket_no, i, ticket_field_name, int(
                    ticket_field_value)])
                ticket_fields[ticket_field_name] = [int(ticket_field_value)]
                ticket_field_names.extend([ticket_field_name])
                ticket_field_invalid = False 
        else: 
            if ticket_field_invalid: 
                invalid_field_val = int(ticket_field_value)
    ticket_fields['invalid'] = invalid_field_val
    checked_tickets[ticket_no] = [ticket_fields, ticket_field_names]

# print(json.dumps(checked_tickets[1], sort_keys=False, indent=4))
ans = 0


for ct in checked_tickets: 
    invalid_value = int(checked_tickets[ct][0].get('invalid'))
    if invalid_value > 0:
        ans += invalid_value
        checked_tickets[ct].pop()
    
# print(ticket_field_positions)
print(ans)

# print(json.dumps(ticket_field_positions, sort_keys=True, indent=4))
def count_field(field_position, field_name):
    fcount = 0
    fvcount = 0
    for t in ticket_field_positions:
        if t[2] == field_name:
            fcount +=1
            if t[1] == field_position:
                fvcount += 1
                # print('pos: %s, name %s\n fpos: %s\n fname: %s\n---\n' %(field_position, field_name, t[1], t[2])) 
    else:
        print(fcount)
        return fvcount

print(count_field(3, 'departure location'))
print(len(checked_tickets))
print(len(ticket_field_positions))
# print(checked_tickets)

# for t in ticket_field_positions:
#     # if 'departure' in t[1]:
#     if t[1] == 3:
#         print(t)
# print(checked_tickets[1])
print(json.dumps(checked_tickets[2], sort_keys=False, indent=4))
