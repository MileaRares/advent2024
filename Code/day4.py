import numpy as np

with open("D:\\Chestii bune\\Advent shit\\inputs\\4.txt", "r") as infile:
    inp = infile.read()

inp = np.array([[e for e in row] for row in inp.strip().split('\n')])

def check_right(i, j):
    if len(inp[0]) - j < 4:
        return False
    result = "".join(inp[i, j:j+4]) == 'XMAS'
    print(f"check_right({i}, {j}): {result}")
    return result

def check_left(i, j):
    if j < 3:
        return False
    result = "".join(inp[i, j-3:j+1]) == 'SAMX'
    print(f"check_left({i}, {j}): {result}")
    return result

def check_up(i, j):
    if i < 3:
        return False
    result = "".join(inp[i-3:i+1, j]) == 'SAMX'
    print(f"check_up({i}, {j}): {result}")
    return result

def check_down(i, j):
    if len(inp) - i < 4:
        return False
    result = "".join(inp[i:i+4, j]) == 'XMAS'
    print(f"check_down({i}, {j}): {result}")
    return result


def check_up_left(i, j):
    if j < 3 or i < 3:
        return False
    result = inp[i-1, j-1] == 'M' and inp[i-2, j-2] == 'A' and inp[i-3, j-3] == 'S'
    print(f"check_up_left({i}, {j}): {result}")
    return result

def check_up_right(i, j):
    if i < 3 or len(inp[0]) - j < 4:
        return False
    result = inp[i-1, j+1] == 'M' and inp[i-2, j+2] == 'A' and inp[i-3, j+3] == 'S'
    print(f"check_up_right({i}, {j}): {result}")
    return result

def check_down_left(i, j):
    if len(inp) - i < 4 or j < 3:
        return False
    result = inp[i + 1, j - 1] == 'M' and inp[i + 2, j - 2] == 'A' and inp[i + 3, j - 3] == 'S'
    print(f"check_down_left({i}, {j}): {result}")
    return result

def check_down_right(i, j):
    if len(inp) - i < 4 or len(inp[0]) - j < 4:
        return False
    result = inp[i+1, j+1] == 'M' and inp[i+2, j+2] == 'A' and inp[i+3, j+3] == 'S'
    print(f"check_down_right({i}, {j}): {result}")
    return result

xmas_nr = 0
for i in range(len(inp)):
    for j in range(len(inp[0])):
        if inp[i][j] == 'X':
            results = [
                check_left(i, j),
                check_up(i, j),
                check_right(i, j),
                check_down(i, j),
                check_up_left(i, j),
                check_up_right(i, j),
                check_down_right(i, j),
                check_down_left(i, j)
            ]
            count = sum(results)
            print(f"X found at ({i}, {j}): {results}, count: {count}")
            xmas_nr += count

print(f"Total XMAS patterns found: {xmas_nr}")
