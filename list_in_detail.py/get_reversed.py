def get_reversed_list(items: list) -> list:
    """
    This function takes a list as an argument and returns the list in reverse order.
    """
    return items[::-1]
get_reversed_list([1, 2, 3]) # [3, 2, 1]
get_reversed_list([70, -2]) # [-2, 70]
print(get_reversed_list([1, 2, 3])) # should return [3, 2, 1]
print(get_reversed_list([70, -2])) # should return [-2, 70
