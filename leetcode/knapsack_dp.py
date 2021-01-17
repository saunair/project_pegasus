




def knapsack_dp(value_set, weight_set, total_weight):
    """Dynammic programming version of the knapsack problem.
    
    Note
    ----
    This solution works only for integers.
    We'll need the branch and bound method to get it to work for floats.

    Parameters
    ----------
    value_set : [int]
    weight_set : [int]
    total_weight : int
    
    Returns
    -------
    int
        Maximum sum weight possible.

    """
    number_of_elements = len(value_set)
    assert number_of_elements == len(weight_set)
    dp_table = [[0 for _ in range(total_weight + 1)] for _ in range(number_of_elements + 1)]
    
    # some initialization is required.
    for row_num in range(1, number_of_elements + 1):
        for current_weight in range(1, total_weight + 1):
            element_weight = weight_set[row_num - 1]
            if element_weight > current_weight:
                dp_table[row_num][current_weight] = dp_table[row_num - 1][current_weight]
            else:
                dp_table[row_num][current_weight] = max(
                    dp_table[row_num - 1][current_weight], # Current element is not chosen.
                    value_set[row_num - 1] + dp_table[row_num - 1][current_weight - element_weight] # Element is chosen.
                )

    return dp_table[number_of_elements][total_weight]


def extended_knapsack_dp(value_set, weight_set, total_allowed_weight, max_number_of_elements):
    """Knapsack with limited number of elements allowed.

    Notes
    -----
    The rows are the number of elements in value_set
    Columns are the number of weights, ranging from 0 to weight_set. 
    The third dimension is solution for the `max_number_of_elements` allowed.
    So this differs a little from the normal version of the knapsack where we link to the previous 3 dimension if the current element is selected.
i   

    Parameters
    ----------
    value_set : [int]
    weight_set : [int]
    total_allowed_weight : int
    max_number_of_elements : int

    Returns
    -------
    int
        Maximum sum weight possible.

    """
    number_of_elements = len(value_set)
    dp_table = [[[0 for _ in range(total_allowed_weight + 1)] for _ in range(number_of_elements + 1)] for _ in range(max_number_of_elements + 1)]
    for row in range(1, len(value_set) + 1):
        for column in range(1, total_allowed_weight + 1):
            for dimension in range(1, max_number_of_elements + 1):
                if column < weight_set[row - 1]:
                    dp_table[dimension][row][column] = dp_table[dimension][row -1][column]
                else:
                    dp_table[dimension][row][column] = max(
                        dp_table[dimension][row -1][column], 
                        dp_table[dimension - 1][row][column - weight_set[row - 1]] + value_set[row - 1]
                    ) 
    
    # We have the solution populated!
    return dp_table[max_number_of_elements][row][column]

# Test case1: plain knapsack, hence total val is 100 + 120 + 2
val = [60, 100, 120, 2] 
wt = [10, 20, 29, 1] 
W = 50
assert knapsack_dp(value_set=val, weight_set=wt, total_weight=W) == 222

# we can choose only two elements, hence 120 + 100 
val = [60, 100, 120, 2] 
wt = [10, 20, 30, 1] 
W = 50
assert extended_knapsack_dp(value_set=val, weight_set=wt, total_allowed_weight=W, max_number_of_elements=2) == 220

