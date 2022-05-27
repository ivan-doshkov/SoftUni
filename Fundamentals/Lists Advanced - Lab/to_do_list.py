notes = input()
todo = ["" for i in range(11)]

while notes != "End":
    explode = notes.split("-")
    importance = int(explode[0])
    note = explode[1]
    todo[importance] = note

    notes = input()

final_todo = [note for note in todo if note != ""]
print(final_todo)
