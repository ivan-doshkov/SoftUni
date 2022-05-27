happiness = input().split(" ")
factor = int(input())
happiness = list(map(int, happiness))
happy = 0
average = 0
for i in happiness:
    score = i * factor
    average = (sum(happiness) * factor) / len(happiness)
    if score >= average:
        happy += 1

if happy >= (len(happiness) / 2):
    print(f"Score: {happy}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {happy}/{len(happiness)}. Employees are not happy!")