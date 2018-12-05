s = open('input.txt').readline().strip()

i = 0
while True:
    c1 = c1 = s[i].lower()
    c2 = c1.upper()
    
    sn = s.replace(c1 + c2, '')
    sn = sn.replace(c2 + c1, '')
    
    i = 0 if s != sn else i + 1
    s = sn
    
    if i == len(s):
        break

print(len(s))
