# day7

input = open('input/day7input.txt', 'r').read()

# pos = input_example.split(',')
pos = input.split(',')

crabs = []
for c in pos: crabs.append(int(c))

csum = sum(crabs)
destinations = list(range(min(crabs), max(crabs)+1, 1))

complete = max(destinations)
fuelc_min = csum**2
efuelc_min = csum**2
for destination in destinations:
    dest_min_fuel = 0
    dest_min_exponential_fuel = 0
    for crab in crabs:
        print(f'{destination} / {complete}', end='\r', flush=True)
        dist = abs(destination-crab)
        edist = dist
        for e in range(0, dist):
            edist += e ** 1
        dest_min_fuel += dist
        dest_min_exponential_fuel += edist
    fuelc_min = min(fuelc_min, dest_min_fuel)
    efuelc_min =  min(efuelc_min, dest_min_exponential_fuel)

print(f'''
lowest consumption:         {fuelc_min}
lowest exp consumption:     {efuelc_min}
''')
