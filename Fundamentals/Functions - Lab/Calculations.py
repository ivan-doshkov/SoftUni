def calculator(operator,a,b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)
    elif operator == "add":
        return  a + b
    elif operator == "subtract":
        return a - b
current_operator = input()
a = int(input())
b = int(input())
print(calculator(current_operator,a,b))