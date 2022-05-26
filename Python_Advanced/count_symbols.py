text = input()

dict1 = dict()

for ch in text:
    if ch not in dict1:
        dict1[ch] = 0
    dict1[ch] += 1

for key, value in sorted(dict1.items()):

    print(f"{key}: {value} time/s")

