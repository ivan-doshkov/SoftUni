grade_data = float(input())
def solve(data):
    if grade_data <3:
        return "Fail"
    elif grade_data <3.5:
        return "Poor"
    elif grade_data <4.5:
        return "Good"
    elif grade_data <5.5:
        return "Very Good"
    else:
        return "Excellent"
print(solve(grade_data))