import aoc

input_data = aoc.fetch_input(2022, 6)


def find_unique_sequence(row, sequence_length):
    for i in range(len(row)):
        row_set = set(row[i - sequence_length:i])
        if len(set(row[i - sequence_length:i])) == sequence_length:
            print(f'found unique set of length {sequence_length}: {row_set}')
            return i


print(f'''
part one: {find_unique_sequence(input_data, 4)}
part two: {find_unique_sequence(input_data, 14)}
''')
