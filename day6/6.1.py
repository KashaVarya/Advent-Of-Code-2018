coords = open('input.txt').read().strip().split('\n')
coords = [list(map(int, line.split(','))) for line in coords]
d_coords = dict()
ids = list()
for i in range(len(coords)):
    d_coords.setdefault(i, coords[i])
    ids.append(i)


def min_manhattan(x, y):
    dist = [(key, abs(coord[0] - x) + abs(coord[1] - y)) for key, coord in d_coords.items()]
    min_dist = min(dist, key=lambda el: el[1])
    return min_dist if [d[1] for d in dist].count(min_dist[1]) == 1 else (-1, -1)


max_x = max(d_coords.items(), key=lambda el: el[1][0])[1][0] + 1
max_y = max(d_coords.items(), key=lambda el: el[1][1])[1][1] + 1

field = list()
field = [field + [0 for x in range(max_x)] for y in range(max_y)]

for y in range(max_y):
    for x in range(max_x):
        field[y][x] = min_manhattan(x, y)[0]

bad_ids = set()
for y in range(max_y):
    bad_ids.add(field[y][0])
    bad_ids.add(field[y][max_x - 1])

for x in range(max_x):
    bad_ids.add(field[0][x])
    bad_ids.add(field[max_y - 1][x])

counts = list([0 for el in range(len(ids))])
for line in field:
    for point in line:
        counts[point] += 1 if point != -1 else counts[point]

for id_coord in bad_ids:
    counts[id_coord] = 0

# for line in field:
#     print(line)
print(max(counts))
