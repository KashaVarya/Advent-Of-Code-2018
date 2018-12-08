def root_value(step, result):
    children = data[step]
    count_metadata = data[step + 1]
    step += 2

    values = dict()
    for i in range(1, children + 1):
        step, result = root_value(step, result)
        values.setdefault(i, result)

    if len(values):
        result = 0
        for i in range(count_metadata):
            index = data[step]
            if index in values:
                result += values[index]
            step += 1
    else:
        result = 0
        for i in range(count_metadata):
            result += data[step]
            step += 1

    return step, result


data = list(map(int, open('input.txt').read().strip().split()))
print(root_value(0, 0)[1])
