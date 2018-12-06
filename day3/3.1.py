import re


lines = open('input.txt').read().strip().split('\n')

size = 1000
wh = [[0 for x in range(size)] for y in range(size)]

for line in lines:
    coord = re.findall(r'\d+', line)
    x = int(coord[1])
    y = int(coord[2])

    lx = int(coord[3])
    wy = int(coord[4])

    for i in range(y, y + wy):
        for j in range(x, x + lx):
            wh[i][j] += 1

# for l in wh:
#     print(l)

good = 0
for s in wh:
    good += s.count(0)
    good += s.count(1)

print(size * size - good)
