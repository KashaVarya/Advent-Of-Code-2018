coords = open('input.txt').read().strip().split('\n')
coords = [list(map(int, line.split(','))) for line in coords]


def all_manhattan(x, y):
    return sum([abs(coord[0] - x) + abs(coord[1] - y) for coord in coords])


max_x = max(coords, key=lambda el: el[0])[0] + 1
max_y = max(coords, key=lambda el: el[1])[1] + 1

dists = list()
for y in range(max_y):
    for x in range(max_x):
        dists.append(all_manhattan(x, y))

max_dist = 1e4
print(sum([1 for dist in dists if dist < max_dist]))
