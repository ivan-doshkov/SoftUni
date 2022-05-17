line = input()
total_price = 0

while line != "special" and line != "regular":
    price = float(line)

    if price < 0:
        print("Invalid price!")
    else:
        total_price += price

    line = input()

taxes = total_price * 0.2
final_price = total_price + taxes
if line == "special":
    final_price = final_price * 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
