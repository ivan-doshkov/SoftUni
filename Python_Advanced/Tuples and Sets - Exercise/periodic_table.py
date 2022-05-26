n = int(input())


ss = set()

for element in range(n):
    el = input().split()
    for i in el:
        ss.add(i)
print('\n'.join(ss))

