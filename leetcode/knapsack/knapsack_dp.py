import tracemalloc

def knapsack_space_optimized_dp(value_set, weight_set, total_weight):
    """Space optimized version of `knapsack_dp`. 
    Here we conciously know that we only need two rows to compute the True/False"""
    # Creating only two rows. 
    dp_table = [[0 for _ in range(total_weight + 1)] for _ in range(2)]
    number_of_elements = len(value_set)
    for row_num in range(1, number_of_elements + 1):
        for current_weight in range(1, total_weight + 1):
            element_weight = weight_set[row_num - 1]
            if row_num % 2 == 0:
                if current_weight < element_weight:
                    dp_table[1][current_weight] = dp_table[0][current_weight]  # Setting from the previous row
                else:
                    dp_table[1][current_weight] = max(
                        dp_table[0][current_weight], 
                        value_set[row_num - 1] + dp_table[0][current_weight - element_weight]
                    )
            else:
                if current_weight < element_weight:
                    dp_table[0][current_weight] = dp_table[1][current_weight]  # Setting from the previous row
                else:
                    dp_table[0][current_weight] = max(
                        dp_table[1][current_weight], 
                        value_set[row_num - 1] + dp_table[1][current_weight - element_weight]
                    )
    return max(dp_table[1][total_weight], dp_table[0][total_weight])


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
    display_knapsack_solution(
        dp_table=dp_table,
        value_set=value_set,
        weight_set=weight_set,
        sack_capacity=total_weight
    )

    return dp_table[number_of_elements][total_weight]


def display_knapsack_solution(dp_table, value_set, weight_set, sack_capacity):
    res = dp_table[len(value_set)][sack_capacity]
    
    current_sack_capacity = sack_capacity
    solution_set = []
    for row_num in range(len(value_set) + 1, 0, -1):
        if res == dp_table[row_num - 1][current_sack_capacity]:
             continue
        solution_set.append(value_set[row_num - 1])
        res = dp_table[row_num - 1][current_sack_capacity - weight_set[row_num - 1]]
        current_sack_capacity = current_sack_capacity - weight_set[row_num - 1]
    print(f"Solution set: {solution_set}")


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
    # Just bounding the problem as the user can give ridiculous inputs. This is not an unbounded knapsack problem.
    max_number_of_elements = min(max_number_of_elements, number_of_elements)
    total_allowed_weight = min(total_allowed_weight, sum(weight_set))

    # Create a 3D dp table. 2D internal table is a singular knapsack table, outer dimension for number of elements allowed.
    dp_table = [
        [
            [0 for _ in range(total_allowed_weight + 1)] for _ in range(number_of_elements + 1)
        ] for _ in range(max_number_of_elements + 1)
    ]
    for dimension in range(1, max_number_of_elements + 1):
        for row in range(1, len(value_set) + 1):
            for current_weight in range(1, total_allowed_weight + 1):
                element_weight = weight_set[row - 1]
                if current_weight < element_weight:
                    dp_table[dimension][row][current_weight] = dp_table[dimension][row -1][current_weight]
                else:
                    #if  dp_table[dimension - 1][row][column - element_weight] + value_set[row - 1] > sum(value_set):
                    dp_table[dimension][row][current_weight] = max(
                        dp_table[dimension][row -1][current_weight], #Current element is not selected.
                        dp_table[dimension - 1][row -1][current_weight - element_weight] + value_set[row - 1]
                    ) 
    return dp_table[max_number_of_elements][row][current_weight]


def unbounded_knapsack(sack_weight_capacity, value_set, weight_set):
    """This is a knapsack with 
    
    Parameters
    ----------
    sack_weight_capacity : int
    value_set : [int]
    weight_set : [int]

    Raises
    ------
    AssertionError
         If lengths of `value_set` and `weight_set` aren't equal.

    Returns
    -------
    int : The maximum value that can go into the sack under the required weight limit.

    """
    assert len(value_set) == len(weight_set), "The properties of the set must have the same length, you dumb fuck"
    dp_table = [0. for _ in range(sack_weight_capacity + 1)]

    for current_weight in range(1, sack_weight_capacity + 1):
        for element_num in range(len(value_set)):
            if weight_set[element_num] <= current_weight:
                dp_table[current_weight] = max(
                    dp_table[current_weight], 
                    dp_table[current_weight - weight_set[element_num]] + value_set[element_num]
                )
    return dp_table[sack_weight_capacity]


if __name__ == "__main__":
    # Test case1: plain knapsack, hence total val is 100 + 120 + 2
    val = [60, 100, 120, 2] 
    wt = [10, 20, 29, 1] 
    W = 50
    tracemalloc.start()
    assert knapsack_dp(value_set=val, weight_set=wt, total_weight=W) == 222
    first_size, first_peak = tracemalloc.get_traced_memory() 
    print(f"size_dp: {first_size}, dp_peak_memory: {first_peak}") 
    # Test case2: space optimized knapsack, hence total val is 100 + 120 + 2
    val = [60, 100, 120, 2] 
    wt = [10, 20, 29, 1] 
    W = 50
    tracemalloc.clear_traces()
    assert knapsack_space_optimized_dp(value_set=val, weight_set=wt, total_weight=W) == 222
    second_size, second_peak = tracemalloc.get_traced_memory() 
    print(f"size_dp_optimized: {second_size}, dp_peak_memory: {second_peak}") 
    
    # we can choose only two elements, hence 120 + 100 
    val = [60, 100, 120, 2] 
    wt = [10, 20, 29, 1] 
    W = 50
    tracemalloc.clear_traces()
    tracemalloc.start()
    ans = extended_knapsack_dp(value_set=val, weight_set=wt, total_allowed_weight=W, max_number_of_elements=2)
    assert ans == 220, f"{ans}, not 220"

    third_size, third_peak = tracemalloc.get_traced_memory() 
    print(f"extended_knapsack: {third_size}, dp_peak_memory: {third_peak}") 
    
    # Ridiculous unconstrained case, but elements cannot repeat.
    val = [60, 100, 120, 2] 
    wt = [10, 20, 29, 1] 
    W = 50
    ans = extended_knapsack_dp(value_set=val, weight_set=wt, total_allowed_weight=70000, max_number_of_elements=1000)
    assert ans == 282, f"{ans}, not 220"

    assert (unbounded_knapsack(sack_weight_capacity=29, value_set=val, weight_set=wt)) == 138
