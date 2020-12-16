import json
# ifile = "day16inputsample.txt"
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
    # print('valid ticket_values for %s:\n %s' %(tva[0], tv_ranges))# print(tv_ranges)


tickets = []
ticket = ticket_data[1].splitlines(False)[1].split(',')
# print(ticket_data[2].splitlines(False)[1].split(','))
for t in ticket_data[2].splitlines(False)[1:]: 
    tickets.append(t.split(','))

import_summary = str('''
ticket values: %s

my ticket: %s

3 first nearby tickets:
%s

all:
%s

''' % (valid_ticket_values, ticket, tickets[0:3], json.dumps(valid_ticket_values, sort_keys=True, indent=4)))

checked_tickets = {}
ticket_no = 0
for nearby_ticket in tickets:
    ticket_no += 1
    # print('-----------\nchecking ticket with fields: %s' % (nearby_ticket))
    invalid_field_val = 0
    for ticket_field in nearby_ticket:
        # print('\nchecking field value: %s' % (ticket_field))
        ticket_field_invalid = True
        ticket_fields = {}
        for ticket_field_name in valid_ticket_values:
            # print('is field with value %s found in %s\n%s' % (ticket_field, ticket_field_name, valid_ticket_values[ticket_field_name]))
            if int(ticket_field) in valid_ticket_values[ticket_field_name]:
                # print('yes!')
                ticket_fields[ticket_field_name] = int(ticket_field)
                ticket_field_invalid = False 
            # else:
                # print('No!')
        else: 
            # print('Ticket field value: %s invalid: %s\n-----------' %
                # (ticket_field, ticket_field_invalid))
            if ticket_field_invalid: 
                invalid_field_val = int(ticket_field)
    # else:
        # print('ticket field value')
            
# else:
    ticket_fields['invalid'] = invalid_field_val
    checked_tickets[ticket_no] = ticket_fields

    # checked_tickets[ticket_no].update({'invalid': invalid_field_val})
        # print('ticket no: %s\n %s' %(ticket_no, checked_tickets[ticket_no]))
# print(tickets[1])
print(json.dumps(checked_tickets, sort_keys=True, indent=4))
ans = 0
for checked_ticket in checked_tickets: 
    # print(checked_tickets[checked_ticket])

    # print(checked_tickets[checked_ticket].get('invalid'))
    ans += int(checked_tickets[checked_ticket].get('invalid'))

print(ans)
# 1731455
