
with open('C:\\Relevant\\advent\\inputa\\5.txt', 'r') as file:
    inp = file.read()

rows = [x for x in inp.strip().split('\n')]

rules = []
updates = []
s = 0

for row in rows:
    if row == '':
        continue
    if '|' in row:
        rules.append([int(row.split('|')[0]), int(row.split('|')[1])])
    else:
        updates.append([int(x) for x in row.split(',')])


for update in updates:
    relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    all_good = True
    for relevant_rule in relevant_rules:
        if not update.index(relevant_rule[0]) < update.index(relevant_rule[1]):
            all_good = False
            break
    if all_good:
        s += update[len(update)//2]

print(s)
