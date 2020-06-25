def ft_filter(function_to_apply, list_of_inputs):
    """Loop over an iterable removing elements
       where the function returns false"""
    pass

    if type(list_of_inputs) not in (tuple, list, set, dict):
        print("Error : Variable is not an iterable.")
        exit(1)
    if not callable(function_to_apply):
        print("Error : Variable is not a function.")
        exit(1)

    result = list_of_inputs.copy()

    if type(list_of_inputs) in (tuple, list, set):
        for k, e in enumerate(list_of_inputs):
            if not function_to_apply(e):
                result.remove(e)
    elif type(list_of_inputs) is dict:
        for e in list_of_inputs:
            if not function_to_apply(list_of_inputs[e]):
                del result[e]
    return result


"""
def isodd(elem):
    return elem % 2 == 0


lst = [1, 2, 3]

print(ft_filter(isodd, lst))
print(lst)
"""
