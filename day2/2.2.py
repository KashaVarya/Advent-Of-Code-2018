lines = open('input.txt').read().strip().split('\n')

for i in range(len(lines) - 1):
    nxt = i + 1
    let_ind = 0
    while True:
        if lines[i][let_ind] != lines[nxt][let_ind]:
            res1 = lines[i][:let_ind] + lines[i][let_ind + 1:]
            res2 = lines[nxt][:let_ind] + lines[nxt][let_ind + 1:]
            if res1 == res2:
                print(res1)
                exit()

            let_ind = 0
            nxt += 1
        elif let_ind == len(lines[i]) - 1:
            break
        else:
            let_ind += 1

        if nxt == len(lines):
            break
