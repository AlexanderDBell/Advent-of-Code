import re

with open('day_1\input.txt') as f:
    input = f.read()

def calibrate(string):
    lines = string.split('\n')
    query = r'[0-9]'
    calibration_code_list = []
    for line in lines:
        first = re.search(query, line).group()
        last = re.search(query, line[::-1]).group()
        calibration_code = int(first+last)
        calibration_code_list.append(calibration_code)
    return sum(calibration_code_list)

print(calibrate(input))
