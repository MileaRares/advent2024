import itertools
from copy import deepcopy

def generate_arrays(l):
    return list(itertools.product([0, 1, 2], repeat=l))

with open("D:\\Chestii bune\\Advent shit\\inputs\\7.txt", "r") as infile:
    inp = infile.read()

inp = [row for row in inp.strip().split('\n')]

sum = 0
for row in inp:
    n = int(row.split(':')[0])
    ps = [int(x) for x in row.split(':')[1].strip().split(' ')]
    stack = []
    for x in ps[::-1]:
        stack.append(x)
    first = stack.pop()
    length = len(stack)
    comb_arrays = generate_arrays(length)
    for comb in comb_arrays:
        result = deepcopy(first)
        s = deepcopy(stack)
        for sign in comb:
            if sign == 0:
                result += s.pop()
            elif sign == 1:
                result *= s.pop()
            elif sign == 2:
                result = int(str(result) + str(s.pop()))
        if result == n:
            sum+=n
            break

print(sum)