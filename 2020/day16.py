ifile = "day16input.txt"
ticket_data = list(open(ifile, 'r').read().split('\n\n'))

ticket_values = {}

for ticket_value in ticket_data[0].splitlines():
    tva = ticket_value.split(': ')
    tvb = tva[1].split(' or ')
    tv_ranges = []
    for tv_range in tvb:
        tv_ranges.append(tv_range.split('-'))

    ticket_values[tva[0]] = tv_ranges
tickets = []
ticket = ticket_data[1].splitlines(False)[1].split(',')
print(ticket_data[2].splitlines(False)[1].split(','))
for t in ticket_data[2].splitlines(False)[1:]: 
    tickets.append(t.split(','))

print('ticket values: %s\n my ticket: %s\n nearby tickets: \n%s' %(ticket_values, ticket, tickets[0:3]))