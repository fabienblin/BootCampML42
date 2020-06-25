def ft_reduce(function_to_apply, list_of_inputs):
    """Loop over an iterable applying the function over each element"""
    pass

    if type(list_of_inputs) not in (tuple, list, set, dict):
        print("Error : Variable is not an iterable.")
        exit(1)
    if not callable(function_to_apply):
        print("Error : Variable is not a function.")
        exit(1)

    it = iter(list_of_inputs)
    value = next(it)
    for element in it:
        value = function_to_apply(value, element)
    return value


"""
lst = [1, 2, 3, 4, 5]

print(ft_reduce(lambda x, y: x+y, lst))

from functools import reduce
print(reduce(lambda x, y: x+y, lst))
"""
