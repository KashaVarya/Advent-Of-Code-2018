data = open('input.txt').read().strip().split('\n')

res, i = 0, 0
s = set()
s.add(0)

while True:
    res += int(data[i])
    sdata = len(s)
    s.add(res)
    if sdata == len(s):
        break 
    i += 1
    if i == len(data):
        i = 0 
        
print(res)

