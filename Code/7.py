with open("D:\\Chestii bune\\Advent shit\\inputs\\2.txt", "r") as infile:
    inp = infile.read()

inp = [row for row in inp.strip().split('\n')]

for row in inp:
    n = row.split(':')[0]
    ps = row.split(':')[1].split(' ')
