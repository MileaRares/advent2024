import re

with open("D:\\Chestii bune\\Advent shit\\inputs\\3.txt", "r") as infile:
    input_text = infile.read()

mul_pattern = r'mul\((\d+),(\d+)\)'
do_pattern = r'do\(\)'
dont_pattern = r'don\'t\(\)'

mul_enabled = True
s = 0

pattern = re.compile(f'{mul_pattern}|{do_pattern}|{dont_pattern}')

for match in pattern.finditer(input_text):
    if re.match(mul_pattern, match.group()):
        if mul_enabled:
            s+= int(match.group()[4:-1].split(',')[0]) * int(match.group()[4:-1].split(',')[1])
    elif re.match(do_pattern, match.group()):
        mul_enabled = True
    elif re.match(dont_pattern, match.group()):
        mul_enabled = False

print(s)
