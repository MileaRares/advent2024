import numpy as np

with open("D:\\Chestii bune\\Advent shit\\inputs\\4.txt", "r") as infile:
    inp = infile.read()

inp = np.array([[e for e in row] for row in inp.strip().split('\n')])

xmas_nr = 0

for i in range(1, len(inp)-1):
    for j in range(1, len(inp[0])-1):
        if inp[i][j] == 'A':
            try:
                if (inp[i-1][j-1] == 'M' and inp[i+1][j+1] == 'S' and inp[i-1][j+1] == 'S' and inp[i+1][j-1] == 'M') or \
                   (inp[i-1][j-1] == 'S' and inp[i+1][j+1] == 'M' and inp[i-1][j+1] == 'M' and inp[i+1][j-1] == 'S') or \
                   (inp[i-1][j-1] == 'M' and inp[i+1][j+1] == 'S' and inp[i-1][j+1] == 'M' and inp[i+1][j-1] == 'S') or \
                   (inp[i-1][j-1] == 'S' and inp[i+1][j+1] == 'M' and inp[i-1][j+1] == 'S' and inp[i+1][j-1] == 'M'):
                    xmas_nr += 1
            except:
                pass

print(f"Total XMAS patterns found: {xmas_nr}")
