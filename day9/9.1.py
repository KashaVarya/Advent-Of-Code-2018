import re


players, marbles = map(int, re.findall(r'\d+', open('input.txt').read()))

field = list([0])
scores = [0 for i in range(1, players + 1)]
current = 0
shift = -7

for i in range(1, marbles + 1):
    if i % 23:
        current = (current + 2) % len(field)
        field.insert(current, i)
    else:
        index = (len(field) + current + shift) % len(field)
        scores[i % players] += i + field[index]
        field.remove(field[index])
        current = index

print(max(scores))
