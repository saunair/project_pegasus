

def two_sum_hash_method(input_array, reqd_sum):
    """Two sum using a hash.

    Complexity
    ----------
    time: O(len(input_array))
    space: O(len(input_array))

    Parameters
    ----------
    input_array: list
    reqd_sum: int 

    Returns
    -------
    bool: If the two sum exists

    """
    two_sum_hash = {}
    for number in input_array:
        if (reqd_sum - number) in two_sum_hash:
            return True
        two_sum_hash[number] = reqd_sum - number 
    return False


if __name__ == "__main__":
    example_array = [10, 102, 1, 4, 6, 2, 3, 4]
    assert two_sum_hash_method(example_array, 5)
    assert two_sum_hash_method(example_array, 9)
    assert not two_sum_hash_method(example_array, -2)
