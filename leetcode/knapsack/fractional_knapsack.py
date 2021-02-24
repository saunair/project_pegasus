from bisect import bisect_right


def fractional_knapsack_with_repetition(total_sack_capacity, value_set, weight_set):
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


class RatioPlaceholder:
    def __init__(self, weight, value):
        self._weight = weight
        self._value = value

    def __repr__(self):
        return f"weight: {self._weight}, value:{self._value}, ratio:{self.ratio}"
    
    @property
    def ratio(self):
        return self._value / self._weight
    
    @property
    def weight(self):
        return self._weight

    @property
    def value(self):
        return self._value


def fractional_knapsack_queries(value_set, weight_set, total_capacity):
    """This solution is a copy of the C++ version in: https://www.geeksforgeeks.org/fractional-knapsack-queries/?ref=rp
    
    Parameters
    ----------
    value_set: 
    weight_set:
    total_sack_capacity: 

    Returns
    -------
    [float] Solutions for each sack capacity
   
    """
    def _pre_process_data(value_set, weight_set):
        element_ratios = []
        for element_weight, element_value in zip(weight_set, value_set):
            element_ratios.append(RatioPlaceholder(weight=element_weight, value=element_value))

        def _sort_by_ratio(element):
            return element.ratio 
        
        element_ratios.sort(key=_sort_by_ratio, reverse=True)
        
        summed_element_ratios = []
        for element_number in range(len(element_ratios)):
            if element_number == 0:
                summed_element = RatioPlaceholder(
                    weight=element_ratios[element_number].weight, 
                    value=element_ratios[element_number].value
                )
            else:
                summed_element = RatioPlaceholder(
                    weight=element_ratios[element_number - 1].weight + element_ratios[element_number].weight,
                    value=element_ratios[element_number - 1].value + element_ratios[element_number].value
                )
            
            summed_element_ratios.append(summed_element)

        return summed_element_ratios

    summed_elements_sorted_by_ratio = _pre_process_data(value_set, weight_set)
    sorted_weights = [element.weight for element in summed_elements_sorted_by_ratio]
    solns = []
    for weight_query in range(total_capacity + 1):
        index = bisect_right(sorted_weights, weight_query, hi=len(sorted_weights))
        if index == 0: # First weight itself exceeds, hence we just use the most optimal one and take a fraction of it.
            soln_for_query = (
                weight_query * 
                summed_elements_sorted_by_ratio[index].value / 
                summed_elements_sorted_by_ratio[index].weight
            )
        else:
            soln_for_query = (
                summed_elements_sorted_by_ratio[index - 1].value + 
                (weight_query - summed_elements_sorted_by_ratio[index - 1].weight) *
                (summed_elements_sorted_by_ratio[index].weight - summed_elements_sorted_by_ratio[index - 1].weight) / 
                (summed_elements_sorted_by_ratio[index].value - summed_elements_sorted_by_ratio[index - 1].value)
            )
        solns.append(soln_for_query)
    return solns
        


if __name__ == "__main__":
    # Driver code
    val = [ 14, 27, 44, 19 ];
    wt = [ 6, 7, 9, 8 ];
    W = 50;
    print(fractional_knapsack_with_repetition(total_sack_capacity=W, weight_set=wt, value_set=val))

    fractional_knapsack_queries(val, wt, W)

