data = open('input.txt').read().strip().split('\n')

res = 0
for num in data:
    res += int(num)
print(res)

