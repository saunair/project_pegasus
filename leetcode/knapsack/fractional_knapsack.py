

def fractional_knapsack(total_sack_capacity, value_set, weight_set):
    """This one allows repetition"""
    # Lame ass problem. You can take fractions of an element! So just use the best element and find its multiplier.
    # I overthought the complexity of the problem. Fuck you geeks for geeks.
    max_fraction = -10000
    max_fraction_index = 0
    for element_number in range(len(value_set)):
        if value_set[element_number] / weight_set[element_number] > max_fraction:
            max_fraction = value_set[element_number] / weight_set[element_number]
            max_fraction_index = element_number
    return total_sack_capacity * max_fraction



if __name__ == "__main__":
    # Driver code
    val = [ 14, 27, 44, 19 ];
    wt = [ 6, 7, 9, 8 ];
    W = 50;
    print(fractional_knapsack(total_sack_capacity=W, weight_set=wt, value_set=val))
