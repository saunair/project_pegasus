"""Given an array the task is to largest divisible subset in array. A subset is called divisible if for every pair (x, y) in subset, either x divides y or y divides x."""



def get_largest_divisible_pair(num_list):
    # If the list doesn't have anything to compute on, return the same.
    if len(num_list) < 2:
        return num_list

    num_list.sort(reverse=False)
    # A table to hold who the previous number is for each.
    previous_element = len(num_list) * [-1]

    # A list to keep count of the previous element in the list.
    number_of_successors = len(num_list) * [0]
    
    #number id would now go across all the lists here.
    for number_id in range(len(num_list)):
        for lower_number_id in range(number_id):
            # Check if the number is compatible, then check for the rest of the criteria "largest".
            if num_list[number_id] % num_list[lower_number_id] == 0:
                # Check if the current number of successors are higher or lower.
                if number_of_successors[number_id] < number_of_successors[lower_number_id] + 1:
                    # Swap the numbers / link to point to this new successor.
                    previous_element[number_id] = lower_number_id
                    number_of_successors[number_id] = number_of_successors[lower_number_id] + 1

    # take an argmax to find the element with the highest succesors.
    biggest_leaf = number_of_successors.index(max(number_of_successors))

    # Now just iterate through the successors to get the set
    largest_divisor_subset = []
    while True:
        current_number = num_list[biggest_leaf]
        largest_divisor_subset.append(current_number)
        if number_of_successors[biggest_leaf] != 0:
            biggest_leaf = previous_element[biggest_leaf]
            # The list is done, now just return
            continue
        # If hit zero successors already, we are at the atomic element of the set.
        break

    return largest_divisor_subset

if __name__ == "__main__":
    assert get_largest_divisible_pair([10, 5, 3, 15, 20]) == [20, 10, 5]
    assert get_largest_divisible_pair([18, 1, 3, 6, 13, 17]) == [18, 6, 3, 1]
    assert get_largest_divisible_pair([2]) == [2]
    assert get_largest_divisible_pair([]) == []
