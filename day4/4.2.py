import re
import operator


lines = open('input.txt').read().strip().split('\n')
lines.sort()

# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up

d, s = dict(), dict()
gn, start = str(), str()
for line in lines:
    digits = re.findall(r'\d+', line)

    if re.search(r'Guard', line):
        gn = digits[5]

    if re.search(r'falls', line):
        start = int(digits[4])

    if re.search(r'wakes', line):
        finish = int(digits[4])
        if gn not in d:
            d.setdefault(gn, [0 for i in range(60)])

        for i in range(start, finish):
            d[gn][i] += 1

max_minute, index, key_res = -1, -1, -1
for key, value in d.items():
    if max_minute < int(max(value)):
        max_minute = max(value)
        index = d[key].index(max_minute)
        key_res = key

print(index * int(key_res))
