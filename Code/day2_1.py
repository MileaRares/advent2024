
with open('C:\\Relevant\\advent\\inputa\\2.txt', 'r') as file:
    input = file.read()

rows = [[int(s) for s in x.split()] for x in input.strip().split('\n') if x.strip()]

ct = 0
for row in rows:
    if len(row) < 2:
        ct += 1
        continue
    if len(row) == 2 and 1 <= abs(row[0] - row[1]) <= 3:
        ct += 1
        continue

    m = 1 if row[0] < row[1] else -1
    cont = False

    for i in range(len(row) - 1):
        if not ((row[i + 1] - row[i]) * m > 0 and 1 <= abs(row[i + 1] - row[i]) <= 3):
            cont = True
            break
    if cont:
        continue
    ct += 1

print(ct)
