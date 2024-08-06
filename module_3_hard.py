def calculate_structure_sum(n):
    sum_ = 0

    if isinstance(n, (int, float)):
        return n
    elif isinstance(n, str):
        return len(n)
    elif isinstance(n, dict):
        for key, value in n.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)
    elif isinstance(n, (list, tuple, set)):
        for item in n:
            sum_ += calculate_structure_sum(item)

    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
