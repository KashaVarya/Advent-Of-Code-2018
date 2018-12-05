s = open('input.txt').readline().strip()

set_s = set(s.lower())
min_units = len(s)
for el in set_s:
    i = 0
    s_work = s.replace(el, '')
    s_work = s_work.replace(el.upper(), '')
    
    while True:
        c1 = s_work[i].lower()
        c2 = c1.upper()
        
        sn = s_work.replace(c1 + c2, '')
        sn = sn.replace(c2 + c1, '')
        
        i = 0 if s_work != sn else i + 1
        s_work = sn
        
        if i == len(s_work):
            break
    
    if len(s_work) < min_units:
        min_units = len(s_work)

print(min_units)
