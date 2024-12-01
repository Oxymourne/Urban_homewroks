data_structure = [

    [1, 2, 3],

    {'a': 4, 'b': 5},

    (6, {'cube': 7, 'drum': 8}),

    "Hello",

    ((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(*args):
    cnt = 0
    for structure in args:
        if isinstance(structure, (int, float)):
            cnt += structure
        elif isinstance(structure, str):
            cnt += len(structure)
        elif isinstance(structure, (list, tuple, set)):
            for element in structure:
                cnt += calculate_structure_sum(element)
        elif isinstance(structure, dict):
            for key, value in structure.items():
                cnt += calculate_structure_sum(key, value)

    return cnt


result = calculate_structure_sum(data_structure)

print(result)