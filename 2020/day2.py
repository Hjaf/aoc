passwords = open('input/day2input.txt', 'r').readlines()

invalid_count = 0
valid_count = 0
for password in passwords:
    raw = password.split(' ')
    required_char = raw[1][0]
    min_count = int(raw[0].split('-')[0])
    max_count = int(raw[0].split('-')[1])
    passwd = raw[2].strip()
    required_char_count = passwd.count(required_char)
    # print('password: "%s" - required character: %s min count: %s max count: %s, password required character count: %s' %(passwd, required_char, min_count, max_count, required_char_count))
    if required_char_count >= min_count and required_char_count <= max_count:
        # print('valid')
        valid_count += 1
    else:
        # print('invalid')
        invalid_count += 1

print(valid_count)


invalid_count = 0
valid_count = 0
for password in passwords:
    raw = password.split(' ')
    required_char = raw[1][0]
    first_position = int(raw[0].split('-')[0])-1
    second_position = int(raw[0].split('-')[1])-1
    passwd = raw[2].strip()
    position_characters = [passwd[first_position], passwd[second_position]]
    # print('password: "%s" - required character: %s at position: %s or position: %s, password position characters: %s, count of correct: %s' %
    #       (passwd, required_char, first_position, second_position, position_characters,  position_characters.count(required_char)))
    if position_characters.count(required_char) == 1:
        # print('valid')
        valid_count += 1
    else:
        # print('invalid')
        invalid_count += 1

print(valid_count)
