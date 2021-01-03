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
    if len(num_list) == 0 or sum_reqd < 0:
        return False

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
