
"""I remember this being asked at my Farmwise interview. I nailed this question using the hash method. But they still needed more with the binary search and sorting method. Sigh."""


def three_sum(number_list, required_sum):
    """Three sum question using hashing method.
    
    Parameters
    ----------
    number_list: list[float]
    required_sum: int

    Returns
    -------
    tuple(float)

    """
    for first_number_index in range(len(number_list)):
        first_number = number_list[first_number_index]
        hash_set = set()
        # The sum to find with two more number other than the first number.
        sum_to_satisfy = required_sum - first_number

        # pretty much two sum problem from here.
        for second_index in range(first_number_index + 1, len(number_list)):
            second_number = number_list[second_index]
            if (sum_to_satisfy - second_number) in hash_set:
                return second_number, first_number, sum_to_satisfy - second_number
            hash_set.add(second_number)
            second_index += 1
    return None, None, None


if __name__ == "__main__":
    number_list = [1, 3, 10, -1]
    print(f"{three_sum(number_list, 3)} for sum: 3")
    number_list = [1, 3, 10, -1]
    print(f"{three_sum(number_list, 12)} for sum: 12")
    number_list = [1, 3, 10, -1]
    print(f"{three_sum(number_list, 14)} for sum: 14")
