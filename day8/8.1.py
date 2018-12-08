def sum_metadata(step, result):
    children = data[step]
    count_metadata = data[step + 1]
    step += 2

    for i in range(children):
        step, result = sum_metadata(step, result)

    for i in range(count_metadata):
        result += data[step]
        step += 1

    return step, result


data = list(map(int, open('input.txt').read().strip().split()))
print(sum_metadata(0, 0)[1])
