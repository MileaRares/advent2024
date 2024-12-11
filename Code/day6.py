with open("D:\\Chestii bune\\Advent shit\\inputs\\6.txt", "r") as infile:
    inp = infile.read()

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


m = [[y for y in x] for x in inp.strip().split('\n')]
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != '^':
            pass
        else:
            start = (i, j)

i, j = start[0], start[1]

moves = 0
while True:
    # print(f"MOVE: {moves}")
    # show_mat(m)
    add_i, add_j = dir_add(m[i][j])
    if not (0 <= i+add_i < len(m) and 0 <= j+add_j < len(m[0])):
        m[i][j] = 'X'
        moves+=1
        # print('')
        break
    if m[i+add_i][j+add_j] == '#':
        m[i][j] = turn(m[i][j])
    else:
        i, j = i+add_i, j+add_j
        m[i][j] = m[i-add_i][j-add_j]
        m[i-add_i][j-add_j] = 'X'

    moves+=1
    # print('')
# print(f"MOVE: {moves}")
# show_mat(m)

x_ct = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 'X':
            x_ct+=1
print(x_ct)
