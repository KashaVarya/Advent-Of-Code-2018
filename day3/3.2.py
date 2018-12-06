import re


lines = open('input.txt').read().strip().split('\n')

size = 1000
wh = [[0 for x in range(size)] for y in range(size)]
coord_l = list()

for line in lines:
    c = re.findall(r'\d+', line)
    coord_l.append(c)

    x1 = int(c[1])
    y1 = int(c[2])
    x2 = int(c[3]) + x1
    y2 = int(c[4]) + y1

    for i in range(y1, y2):
        for j in range(x1, x2):
            wh[i][j] += 1

for c in coord_l:
    good = True
    x1 = int(c[1])
    y1 = int(c[2])
    x2 = int(c[3]) + x1
    y2 = int(c[4]) + y1

    for i in range(y1, y2):
        for j in range(x1, x2):
            if wh[i][j] != 1:
                good = False
                break
        if not good:
            break
    if good:
        print(c[0])
        exit()
