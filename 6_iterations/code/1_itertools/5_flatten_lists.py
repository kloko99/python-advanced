import itertools as it

# Eine Ebene flatten


def flatten(list_of_lists):
    "Flatten one level of nesting"
    return it.chain(*list_of_lists)
    # return it.chain.from_iterable(list_of_lists)


def flatten_extend(list_of_lists):
    out = []
    for list_ in list_of_lists:
        out.extend(list_)
    return out


def flatten_recursive(deep_list):
    result = []
    for el in deep_list:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten_recursive(el))
        else:
            result.append(el)
    return result


a = [["a", "b"], [2, 3]]
print("it chain:", list(flatten(a)))  # ['a', 'b', 2, 3]
print("extend:", flatten_extend(a))  # ['a', 'b', 2, 3]

deep_list = [[["a", "bib"], [2, 3]], [["c", "d"], [4, 5, [7, 9]]]]
print(flatten_recursive(a))
print(flatten_recursive(deep_list))
