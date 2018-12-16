import re

file = open('input.txt')
initial = re.findall(r'initial\sstate:\s(.*)', file.readline().strip())[0]

rules = [rule for rule, res in re.findall(r'(.{5})\s=>\s(.)', file.read().strip()) if res != '.']

generations = 20
empty = '.....'
start = 0
work = str()
for i in range(generations):
    if not initial[:5] == empty:
        initial = empty + initial
        start += 5
    if not initial[-5:] == empty:
        initial = initial + empty
    work = initial
    for j in range(len(work)):
        work = work[:j] + '.' + work[j + 1:]

    for rule in rules:
        begin = 0
        while True:
            index = initial.find(rule, begin)
            if index == -1:
                break
            else:
                work = work[:index + 2] + '#' + work[index + 3:]
                begin = index + 1
    initial = work
print(work)

ans = 0
for i in range(len(work)):
    if work[i] == '#':
        ans += i - start
print(ans)
