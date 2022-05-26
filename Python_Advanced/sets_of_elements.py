lens = input().split()
s1 = set()
s2 = set()
s3 = set()
for i in range(int(lens[0])):
    num1 = int(input())
    s1.add(num1)
for n in range(int(lens[1])):
    num2 = int(input())
    s2.add(num2)

for element in s1:
    if element in s2:
        s3.add(element)
ss = map(str, s3)
print("\n".join(ss))