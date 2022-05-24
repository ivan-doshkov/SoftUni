factor = int(input())
count = int(input())
num_list = []

for i in range(1, count + 1):
    current = i * factor
    num_list.append(current)

print(num_list)
