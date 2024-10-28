def filter_list(l):
    'return a new list with the strings filtered out'
    return [num for num in l if not isinstance(num, str)]