import re
passports = open('input/day4input.txt', 'r').read().split('\n\n')

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
alternate_fields = ['cid']

field_requirements = {
    "byr": {"required": True, "format": r"\d{4}", "min": 1920, "max": 2002},
    "iyr": {"required": True, "format": r"\d{4}", "min": 2010, "max": 2020},
    "eyr": {"required": True, "format": r"\d{4}", "min": 2020, "max": 2030},
    "hgt": {"required": True, "format": r"(\d{2,3}(cm|in){1})", "min": {"cm": 150, "in": 59}, "max": {"cm": 193, "in": 76}},
    "hcl": {"required": True, "format": r"(#[\da-f]{6})", "min": False, "max": False},
    "ecl": {"required": True, "format": r"(amb|blu|brn|gry|grn|hzl|oth){1}", "min": False, "max": False},
    "pid": {"required": True, "format": r"\d{9}", "min": False, "max": False},
    "cid": {"required": False, "format": "", "min": False, "max": False}
}

valid_passports = []
valid_count = 0
fields_present_count = 0
for p in passports:
    valid = True
    fields_present = True
    passport = p.split()
    fields = {}

    for f in passport:
        fields[f.split(':')[0]] = f.split(':')[1]

    for field in field_requirements:
        f_req =  field_requirements[field]
        f_req_format = re.compile(f_req.get('format'))
        f_req_min = f_req['min']
        f_req_max = f_req['max']
        if f_req.get('required'):
            if field in fields: # continue if required field is present.
                field_value = fields[field]
                if not f_req_format.fullmatch(field_value):
                    # print('field: %s value: %s not matching format: %s' %
                    #       (field, field_value, f_req.get('format')))
                    valid = False
                elif type(f_req['max']) == dict: # unit is specified if max / min is a dict
                    f_max_units = f_req['max'].keys()
                    for unit in f_max_units:
                        if unit in field_value:
                            int_field_value = int(field_value[:-len(unit)])
                            if int_field_value > f_req_max[unit] or int_field_value < f_req_min[unit]:
                                valid = False
                elif (f_req_max or f_req_min): # else if max / min is value.
                    if int(field_value) > f_req_max or int(field_value) < f_req_min:
                        valid = False
            else: #field is required but not found in passport fields.
                fields_present = False
        
    if valid and fields_present:
        valid_count += 1
    if fields_present:
        fields_present_count += 1
    # print('passport:\n %s\n required fields present: %s fields valid: %s\n----------' %(passport, fields_present, valid))

# part one
print('part one answer: %s' %(fields_present_count))

# part 
print('part two answer: %s' %(valid_count))

