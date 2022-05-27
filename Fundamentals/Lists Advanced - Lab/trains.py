wagons = int(input())
trains = [0] * wagons
comand = input()
while comand != "End":
    explode = comand.split(" ")
    type = explode[0]
    if type == "add":
        people = int(explode[1])
        trains[len(trains) - 1] += people
    if type == "insert":
        position = int(explode[1])
        people = int(explode[2])
        trains[position] += people
    if type == "leave":
        position = int(explode[1])
        people = int(explode[2])
        trains[position] -= people

    comand = input()
print(trains)
