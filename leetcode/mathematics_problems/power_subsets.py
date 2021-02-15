"""Power Set Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
If S has n elements in it then P(s) will have 2^n elements"""



def generate_power_sets(sample_list):
    """Generate all possible subsets from the `sample_list`.

    Parameters
    ----------
    sample_list : [int]
    
    Returns
    -------
    [[int]]
        All possible subsets
    
    """
    num_of_combinations = pow(2, len(sample_list))
    all_sets = []
    for element_number in range(num_of_combinations):
        set_for_number = []
        for binary_num in range(len(sample_list)):
            if (1 << binary_num) & element_number:
                set_for_number.append(sample_list[binary_num])
        all_sets.append(set_for_number)
    return all_sets



if __name__ == "__main__":
    a = ["a", "b", "c"]
    b = generate_power_sets(a) 
