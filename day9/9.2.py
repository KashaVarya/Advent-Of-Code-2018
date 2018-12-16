import re


players, marbles = map(int, re.findall(r'\d+', open('input.txt').read()))
marbles *= 100

field = list([0])
scores = [0 for i in range(1, players + 1)]
current = 0
shift = -7

ans = list()

for i in range(1, marbles + 1):
    if i % 23:
        # print('i', i, ' curr', current, ' len', len(field))

        current = (current + 2) % len(field)
        field.insert(current, i)
    else:
        index = (len(field) + current + shift) % len(field)
        scores[i % players] += i + field[index]
        field.remove(field[index])
        current = index
        # print(field)

        ans.append(max(scores))
        print('i', i, ' ans', max(scores))



# print(field)
m = max(scores)
for i in range(len(scores)):
    if m == scores[i]:
        print(i)
        print(scores[i])

# for i in range(1, len(ans)):
#     if ans[i] != ans[i - 1]:
#         print(ans[i] - ans[i - 1])
