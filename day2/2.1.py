lines = open('input.txt').read().strip().split('\n')

t1, t2 = False, False
r1, r2 = 0, 0

for line in lines:
    t1, t2 = False, False
    for let in line:
        if line.count(let) == 2 and not t1:
            t1 = True
            r1 += 1
        if line.count(let) == 3 and not t2:
            t2 = True
            r2 += 1
        if t1 and t2:
            t1, t2 = False, False
            break

print(r1 * r2)
