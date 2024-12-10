from copy import deepcopy

with open("D:\\Chestii bune\\Advent shit\\inputs\\2.txt", "r") as infile:
    input = infile.read()

input = [[int(e) for e in row.split()] for row in input.strip().split('\n')]

def is_good(row):
    diffs = [(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    return (max([abs(d) for d in diffs]) <= 3 and min([abs(d) for d in diffs]) >= 1 and
            (sorted(row) == row or sorted(row, reverse=True) == row))


ct = 0
for row in input:
    diffs = []
    if is_good(row[1:]) or is_good(row[:-1]):
        ct+=1
        continue

    for i in range(len(row)-1):
        diffs.append(row[i] - row[i + 1])

    cont = False

    plus, minus = 0, 0
    for i, d in enumerate(diffs):
        if d > 0:
            plus +=1
        elif d < 0:
            minus +=1

        # means more than 1 deletions necessary
        if plus > 1 and minus > 1:
            cont=True
            break

        if (min([minus, plus]) == 1 and max([minus, plus]) > 1) or d == 0 or abs(d) > 3:
            r1, r2 = deepcopy(row), deepcopy(row)
            r1 = r1[:i] + r1[(i+1):]
            r2 = r2[:(i+1)] + r2[(i+2):]
            if is_good(r1) or is_good(r2):
                ct+=1
                cont = True
                break
            else:
                cont = True
                break

    if cont:
        continue

    ct+=1

print(ct)