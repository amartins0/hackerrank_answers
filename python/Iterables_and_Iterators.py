from itertools import combinations


n, s, k = input(), input().split(), int(input())
combs = list(combinations(s, k))
a_filter = filter(lambda f: 'a' in f, combs)

print("{:.4}".format((len(list(a_filter))/len(combs))))