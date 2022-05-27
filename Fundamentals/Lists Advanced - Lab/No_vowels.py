list1 = input()
list2 = ['a', 'o', 'u', 'e', 'i']
list3 = list()
for i in list1:
    if i not  in list2:
        list3.append(i)
print("".join(list3))


