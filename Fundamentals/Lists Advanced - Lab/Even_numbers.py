number_list = list(map(int, input().split(", ")))
new_list = []
for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        new_list.append(i)
print(new_list)
