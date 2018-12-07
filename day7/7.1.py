import re


insts = open('input.txt').read().strip().split('\n')

insts_dict = dict()
steps = set()
ready = list()
result = str()

for inst in insts:
    who, before = re.findall(r'\s([A-Z])\s', inst)
    steps.add(who)
    steps.add(before)
    if before not in insts_dict:
        insts_dict.setdefault(before, [who])
    else:
        insts_dict[before].append(who)

for step in steps:
    if step not in insts_dict:
        ready.append(step)

while len(ready):
    ready.sort()
    step = ready[0]
    result += step
    ready.pop(0)

    for key, values in insts_dict.items():
        if step in values:
            values.remove(step)

            if not len(values):
                ready.append(key)

print(result)
