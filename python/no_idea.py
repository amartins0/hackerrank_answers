n, m = input().split()
s = input().split()
a = set(input().split())
b = set(input().split())

print(sum([(i in a) - (i in b) for i in s]))