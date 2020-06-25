def ft_map(function_to_apply, list_of_inputs):
    """Loop over an iterable applying the function over each element"""
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
            result[k] = function_to_apply(e)
    elif type(list_of_inputs) is dict:
        for e in result:
            result[e] = function_to_apply(result[e])
    return result


"""
def addone(elem):
    return elem+1

lst={"a":1, "b":2, "c":3}

print(ft_map(addone, lst))
print(lst)
"""
