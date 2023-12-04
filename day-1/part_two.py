import re

with open('day_1\input.txt') as f:
    input = f.read()

numbers_dict = {
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
}

def calibrate(string):
    lines = string.split('\n')
    query = r'[0-9]|one|two|three|four|five|six|seven|eight|nine'
    rquery = r'[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'
    calibration_code_list = []
    for line in lines:
        first = re.search(query, line).group()
        last = re.search(rquery, line[::-1]).group()[::-1]
        calibration_code = int(numbers_dict.get(first,first))*10+int(numbers_dict.get(last,last))
        calibration_code_list.append(calibration_code)
    return sum(calibration_code_list)

print(calibrate(input))
