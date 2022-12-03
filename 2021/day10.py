#
input_file = open('input/day10input.txt', 'r').readlines()
input = []
for row in input_file:
    input.append(row.strip())

scores = dict({
    '<': 25137,
    '>': 25137,
    '{': 1197,
    '}': 1197,
    '[': 57,
    ']': 57,
    '(': 3,
    ')': 3
})

points = dict({
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
})
characters_pairs = dict({
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
})

############### part 1 ################
total_score = 0
characters_log = {}
incomplete_input = {}
for li, line in enumerate(input):
    line_char_buffer = []
    line_char_score = 0
    closing_characters = list(characters_pairs.keys())
    for ci, char in enumerate(line):
        if char in closing_characters:
            characters_log[ci] = characters_pairs[char]
            line_char_buffer.append(characters_pairs[char])
        elif line_char_buffer[-1] == char:
            line_char_buffer.pop()
        else:
            line_char_score = scores[char]
            line_char_buffer = []
            break

    total_score += line_char_score
    if line_char_buffer.__len__() > 0:
        incomplete_input[li] = list(line_char_buffer)

print(total_score)


############### part 2 ################
total_cost = []
for incomplete in incomplete_input:
    cost = 0
    a_complete = list(incomplete_input[incomplete])
    a_complete.reverse()
    for ci, char in enumerate(a_complete):
        cost = cost * 5 + points[char]
    total_cost.append(cost)
middle = int((len(total_cost))/2)
total_cost.sort()
total_cost[middle]
