"""Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.

Examples:

Input : arr[] = {2, 3, 5, 6, 8, 10}
        sum = 10
Output : 5 2 3
         2 8
         10

Input : arr[] = {1, 2, 3, 4, 5}
        sum = 10
Output : 4 3 2 1 
         5 3 2 
         5 4 1 
"""


def does_subset_exist_for_sum(num_list, sum_reqd):
    """ The recursive solution to find if `sum_reqd` exists in `num_list`.
    
    Parameters
    ----------
    num_list : list
        List of positive integers
    sum_reqd : int

    Returns
    -------
    bool : True if the `sum_reqd` subset exists in `num_list` .

    """
    
    if sum_reqd == 0:
        return True

    # If the list is null or the sum has gone negative
    if len(num_list) == 0 or sum_reqd < 0:
        return False
    
    # Sum asked is positive, keep searching with and without the last element.
    # either the last number is part of the solution for the sum or doesn't.
    return (
        does_subset_exist_for_sum(num_list=num_list[:-1], sum_reqd=sum_reqd) or 
        does_subset_exist_for_sum(num_list=num_list[:-1], sum_reqd=sum_reqd-num_list[-1])
    )


def does_subset_exist_for_sum_from_power_sets(num_list, sum_reqd):
    """Similar to the brute force solution, but we create all the subsets first and then check the sums
    
    Parameters
    ----------
    num_list : list
    sum_reqd : int

    Returns
    -------
    bool : True if the `sum_reqd` subset exists in `num_list` .
    
    """

    from power_subsets import generate_power_sets
    all_subsets = generate_power_sets(num_list)
    all_sums = [sum(subset) for subset in all_subsets]
    try:
        all_sums.index(sum_reqd)
    except ValueError:
        return False
    return True
   

def does_subset_exist_for_sum_dp(num_list, sum_reqd):
    """A dynammic program version of the sum done in the apis 
    `does_subset_exist_for_sum_from_power_sets` and `does_subset_exist_for_sum`. 
    
    Solution is inspired from the one in geeks for geeks.

    Parameters
    ----------
    num_list : list
    sum_reqd : int

    Returns
    -------
    bool : True if the `sum_reqd` subset exists in `num_list` .
    
    """
    numbers_in_set = len(num_list)
    # Create a table with (len(num_list) + 1) * (sum_reqd + 1)) booleans to track the possibility of sum.
    # Columns designate a `sum` and the rows designate the numbers from the set. 
    subset_sum_table = [[False for i in range(sum_reqd + 1)]  for j in range(numbers_in_set + 1)] 
    
    # For a sum of 0, all elements are fine as the length of the array is `0`.
    # Hence first row must remain all False.
    for i in range(numbers_in_set + 1):
        subset_sum_table[i][0] = True
     
    # Filling the table from the sum of 0.
    # start the row num from 1 as we have inserted a 0 the in the beginning for an empty set
    # Start the column num from 1 as the first column corresponds to sum 0 which is already num_rows * [True]
    for row_num in range(1, numbers_in_set + 1):
        for current_sum in range(1, sum_reqd + 1): # "sum_reqd + 1" as we want to go up to `sum_reqd` columns. 
            current_number_from_set = num_list[row_num - 1] # -1 as the row_num has 0 in the first index for a null set.
            
            # If the sum is lower than the number in the list, just use the result of the previous number in the list.
            if current_sum < current_number_from_set: 
                subset_sum_table[row_num][current_sum] = subset_sum_table[row_num - 1][current_sum]
            # Now either we check if the previous number satisfies the req or we reiterate to sum - current_number_from_set.
            elif current_sum >= current_number_from_set:
                subset_sum_table[row_num][current_sum] = (
                    subset_sum_table[row_num - 1][current_sum] or 
                    subset_sum_table[row_num - 1][current_sum - current_number_from_set]
                )
    return subset_sum_table[numbers_in_set][sum_reqd]


# Test cases
test_list = [1, 10, 3, 4]
assert (does_subset_exist_for_sum(test_list, 1))
assert (does_subset_exist_for_sum(test_list, 11))
assert not (does_subset_exist_for_sum(test_list, 12))

test_list = [1, 2, 3, 4, 5]
assert (does_subset_exist_for_sum(test_list, 10))
assert (does_subset_exist_for_sum(test_list, 4))
assert not (does_subset_exist_for_sum(test_list, 16))

assert (does_subset_exist_for_sum_from_power_sets(test_list, 10))
assert (does_subset_exist_for_sum_from_power_sets(test_list, 4))
assert not (does_subset_exist_for_sum_from_power_sets(test_list, 16))

# DP tests.
test_list = [3, 34, 4, 12, 5, 2]
assert (does_subset_exist_for_sum_dp(test_list, 0))
assert (does_subset_exist_for_sum_dp(test_list, 3))
assert (does_subset_exist_for_sum_dp(test_list, 37))
assert (does_subset_exist_for_sum_dp(test_list, 38))
assert not (does_subset_exist_for_sum_dp(test_list, 500))


test_list = [1, 2, 3, 4, 5]
assert (does_subset_exist_for_sum_dp(test_list, 10))
assert (does_subset_exist_for_sum_dp(test_list, 0))
assert not (does_subset_exist_for_sum_dp(test_list, 16))
assert not (does_subset_exist_for_sum_dp(test_list, 999))

