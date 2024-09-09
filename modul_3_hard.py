data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

def calculate_structure_sum(*args):
    structure_sum = 0
    for arg in args:
        if isinstance(arg, str):
            structure_sum += len(arg)
        elif isinstance(arg, int):
            structure_sum += arg
        elif isinstance(arg, list):
            structure_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, tuple):
            structure_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, set):
            structure_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            structure_sum += calculate_structure_sum(*arg.items())
        elif arg is None:
            pass
    return structure_sum

result = calculate_structure_sum(data_structure)
print(result)