import itertools

with open("D:\\Chestii bune\\advent2024\\inputs\\8.txt", "r") as infile:
    inp = infile.read()

m = [[y for y in x] for x in inp.strip().split('\n')]

antennas = dict()
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != '.':
            antennas.setdefault(m[i][j], []).append((i,j))


antinodes_positions = set()
for positions in antennas.values():
    for pos1, pos2 in (itertools.combinations(positions, 2)):
        x_diff = pos1[0] - pos2[0]
        y_diff = pos1[1] - pos2[1]
        if 0 <= pos2[0] - x_diff < len(m) and 0 <= pos2[1] - y_diff < len(m[0]):
            antinodes_positions.add((pos2[0] - x_diff, pos2[1] - y_diff))
        if 0 <= pos1[0] + x_diff < len(m) and 0 <= pos1[1] + y_diff < len(m[0]):
            antinodes_positions.add((pos1[0] + x_diff, pos1[1] + y_diff))

print(len(antinodes_positions))

