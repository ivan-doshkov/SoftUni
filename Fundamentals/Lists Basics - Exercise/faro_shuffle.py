deck = input().split()
shuffle_count = int(input())

deck_list = []

for i in range(shuffle_count):
    deck_list = []
    middle_deck = len(deck) // 2
    part_1 = deck[:middle_deck]
    part_2 = deck[middle_deck::]

    for n in range(len(part_1)):
        deck_list.append(part_1[n])
        deck_list.append(part_2[n])
        deck = deck_list
print(deck)
