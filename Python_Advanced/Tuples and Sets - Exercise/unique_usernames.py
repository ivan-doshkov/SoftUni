num = int(input())

s = set()

for n in range(num):
    name = input()
    s.add(name)

print("\n".join(s))
    