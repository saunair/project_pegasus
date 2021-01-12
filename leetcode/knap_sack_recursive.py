## The recursive solution to the 0-1 knapsack problem.


def knapsack_recursive(element_values, element_weights, max_weight_capacity):
    """ A recursive solution to the knapsack problem.
    
    Parameters
    ----------
    element_values : [int]
    element_weights : [int]
    max_weight_capacity : int

    Returns
    -------
    [int]
        The values that fix the best within `max_weight_capacity`

    """
    assert max_weight_capacity >=0
    assert len(element_values) == len(element_weights)
   
    if max_weight_capacity == 0 or len(element_weights) == 0:
        return []
    
    # Capacity is lower than the weight of the final element.
    if max_weight_capacity < element_weights[-1]:
       return knapsack_recursive(
           element_values=element_values[:-1], 
           element_weights=element_weights[:-1], 
           max_weight_capacity=max_weight_capacity
       ) 
    
    elements_with = [element_values[-1]]
    b = knapsack_recursive(
        element_values=element_values[:-1], 
        element_weights=element_weights[:-1], 
        max_weight_capacity=max_weight_capacity - element_weights[-1]
    )
    elements_with += b
    elements_without = knapsack_recursive(
        element_values=element_values[:-1], 
        element_weights=element_weights[:-1], 
        max_weight_capacity=max_weight_capacity
    )

    if sum(elements_with) >= sum(elements_without):
        return elements_with
    
    return elements_without


element_values = [60, 100, 120]
element_weights = [10, 20, 30]
max_weight_capacity = 50
knap_sack_result = knapsack_recursive(
    element_values=element_values, 
    element_weights=element_weights, 
    max_weight_capacity=max_weight_capacity
)
assert knap_sack_result == [120, 100]
