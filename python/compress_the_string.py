from itertools import groupby


s = str(input())

key_function = lambda x: x[0]

for key, group in groupby(s, key_function):
    print(*[(len(list(group)), int(key))], end=' ')