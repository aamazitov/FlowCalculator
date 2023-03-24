def get_min_index_from_list(src_list: list, src_value: float = None) -> int:
    ind = 0

    if src_value:
        diff = 1000000000000000000

        for i in range(len(src_list)):
            if diff > abs(src_list[i] - src_value):
                diff = abs(src_list[i] - src_value)
                ind = i
    else:
        ind = len(src_list) - 1

    return ind
