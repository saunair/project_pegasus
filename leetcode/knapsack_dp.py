




def knapsack_dp(value_set, weight_set, total_weight):
    """Dynammic programming version of the knapsack problem"""
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


val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
print(knapsack_dp(value_set=val, weight_set=wt, total_weight=W))  
