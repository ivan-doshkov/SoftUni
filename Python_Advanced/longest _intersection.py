def gen_seq(range_info):
    start, end = [int(x) for x in range_info.split(',')]
    return set(range(start, end + 1))


n = int(input())

best_intersection = set()

for i in range(n):
    line_parts = input().split("-")
    first_set = gen_seq(line_parts[0])
    sec_set = gen_seq(line_parts[1])
    current_set = first_set.intersection(sec_set)
    if len(current_set) > len(best_intersection):
        best_intersection = current_set
print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}] with length {len(best_intersection)}")
