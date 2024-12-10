import re


with open("D:\\Chestii bune\\Advent shit\\inputs\\3.txt", "r") as infile:
    input = infile.read()

pattern = r'mul\(\d+,\d+\)'
matches = re.finditer(pattern, input)
s = 0
for match in matches:
    mul_string = match.group()[4:-1]
    s+= int(mul_string.split(',')[0]) * int(mul_string.split(',')[1])

print(s)