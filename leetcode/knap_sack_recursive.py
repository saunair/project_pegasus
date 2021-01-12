## The recursive solution to the 0-1 knapsack problem.



def knapsack_recursive(element_values, element_weights, max_weight_capacity):
    """
    
    Parameters
    ----------
    element_values : [int]
    element_weights : [int]
    max_weight_capacity : int

    """
    assert max_weight_capacity >=0
    assert len(element_values) == len(element_weights)
   
    if max_weight_capacity == 0 or len(element_weights) == 0:
        return 0
    # Capacity is lower than the weight of the final element.
    if max_weight_capacity < element_weights[-1]:
       return knapsack_recursive(
           element_values=element_values[:-1], 
           element_weights=element_weights[:-1], 
           max_weight_capacity=max_weight_capacity
       ) 

    return max(
        element_values[-1] + knapsack_recursive(
            element_values=element_values[:-1], 
            element_weights=element_weights[:-1], 
            max_weight_capacity=max_weight_capacity - element_weights[-1]
        ), 
        knapsack_recursive(
            element_values=element_values[:-1], 
            element_weights=element_weights[:-1], 
            max_weight_capacity=max_weight_capacity
        )
    )



element_values = [60, 100, 120]
element_weights = [10, 20, 30]
max_weight_capacity = 50
a = knapsack_recursive(element_values=element_values, element_weights=element_weights, max_weight_capacity=max_weight_capacity)
print(a)
