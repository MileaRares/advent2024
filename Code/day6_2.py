from copy import deepcopy


def turn(d):
    turn_dir = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }
    return turn_dir[d]

def dir_add(d):
    dir_dict = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    return dir_dict[d]

def show_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end='')
        print('')

# with open("D:\\Chestii bune\\Advent shit\\inputs\\test.txt", "r") as infile:
#     inp = infile.read()

with open("C:\\Relevant\\advent2024\\inputa\\6.txt", "r") as infile:
    inp = infile.read()

m = [[y for y in x] for x in inp.strip().split('\n')]

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != '^':
            pass
        else:
            start = (i, j)
            break

i, j = start[0], start[1]

wall_ct = 0
moves = 0
turning_dir = {}

while True:
    # print(f"MOVE: {moves}")
    # show_mat(m)
    add_i, add_j = dir_add(m[i][j])
    if not (0 <= i+add_i < len(m) and 0 <= j+add_j < len(m[0])):
        # m[i][j] = 'X'
        # print('')
        break
    if m[i+add_i][j+add_j] == '#' or m[i+add_i][j+add_j] == '$':
        turning_dir.setdefault((i + add_i, j + add_j), set()).add(m[i][j])
        m[i][j] = turn(m[i][j])
        m[i + add_i][j + add_j] = '$'
    else:
        i, j = i+add_i, j+add_j
        m[i][j] = m[i-add_i][j-add_j]
        m[i-add_i][j-add_j] = '.'

m[0][21] = '.'
m[start[0]][start[1]] = '^'
m_copy = deepcopy(m)
show_mat(m)
i, j = start[0], start[1]

while True:

    add_i, add_j = dir_add(m[i][j])
    if not (0 <= i+add_i < len(m) and 0 <= j+add_j < len(m[0])):
        m[i][j] = 'X'
        moves+=1
        # print('')
        break

    if m[i+add_i][j+add_j] == '#' or m[i+add_i][j+add_j] == '$':
        m[i+add_i][j+add_j] = '$'
        m[i][j] = turn(m[i][j])
    else:
        x, y = deepcopy(i), deepcopy(j)
        pos_dir_add_x, pos_dir_add_y = dir_add(turn(m[i][j]))
        x += pos_dir_add_x
        y += pos_dir_add_y
        while 0 <= x < len(m) and 0 <= y < len(m[0]):
            if m[x][y] == '$' and turn(m[i][j]) in turning_dir[(x, y)]:
                wall_ct += 1
                # print(f"CAN ADD ON: {i, j}")
                m_copy[i+add_i][j+add_j] = '$'
                # show_mat(m_copy)
                m_copy[i+add_i][j+add_j] = m[i+add_i][j+add_j] if m[i+add_i][j+add_j] == '#' else '^' if (i+add_i, j+add_j) == (start[0], start[1]) else '.'

                break
            x += pos_dir_add_x
            y += pos_dir_add_y

        i, j = i+add_i, j+add_j
        m[i][j] = m[i-add_i][j-add_j]
        m[i-add_i][j-add_j] = 'X'

    moves+=1

# show_mat(m)

print(wall_ct)
