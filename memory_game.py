energy = int(input())
distance = input()

counter_win = 0
cond = True

while distance != "End of battle":
    current_distance = int(distance)

    if energy < current_distance:
        print(f"Not enough energy! Game ends with {counter_win} won battles and {energy} energy")
        cond = False
        break
    counter_win += 1
    energy -= current_distance
    if counter_win % 3 == 0:
        energy += counter_win

    distance = input()
if cond:
    print(f"Won battles: {counter_win}. Energy left: {energy}")
