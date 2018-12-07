import re


class Worker:
    task = ''
    finish = 0


insts = open('input.txt').read().strip().split('\n')

insts_dict = dict()
steps = set()
ready = list()
result = str()
workers_count = 5
workers = list()

for i in range(workers_count):
    w = Worker()
    workers.append(w)

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

while len(result) != len(steps):

    busy_workers = [w for w in workers if w.task != '']
    if len(busy_workers):
        stop_worker = min(busy_workers, key=lambda w: w.finish)
        if stop_worker.task != '':
            result += stop_worker.task

            for worker in workers:
                if worker.task == '':
                    worker.finish = stop_worker.finish

            for key, values in insts_dict.items():
                if stop_worker.task in values:
                    values.remove(stop_worker.task)

                    if not len(values):
                        ready.append(key)

            stop_worker.task = ''

    ready.sort()
    for worker in workers:
        if len(ready) and worker.task == '':
            worker.task = ready[0]
            ready.pop(0)
            worker.finish += ord(worker.task) - 64 + 60

print(result)
print(max(workers, key=lambda w: w.finish).finish)
