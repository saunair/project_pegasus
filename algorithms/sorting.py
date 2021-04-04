from copy import copy


def bubble_sort(array, in_array_sort=True):
    if not in_array_sort:
        memory_array = copy(array)
    else:
        memory_array = array

    count = 0

    while (len(memory_array) - count) > 0:
        inner_index = 0
        while inner_index < len(memory_array) - 1 - count :
            if memory_array[inner_index] > memory_array[inner_index + 1]:
                # Swap the values in place.
                memory_array[inner_index + 1], memory_array[inner_index] = memory_array[inner_index], memory_array[inner_index + 1]
            inner_index += 1
        # Last element is the highest one, so the loop terminates earlier next time.
        count += 1
    return memory_array


def _sort_and_merge_sub_arrays(left_array, right_array):
    """This method assumes elements in `left_array` and `right_array` are already sorted.
    
    Parameters
    ----------
    left_array: list[int]
    right_array: list[int]

    Returns
    -------
    list: merged and sorted list 

    """
    left_array_length = len(left_array)
    right_array_length = len(right_array) 
    
    # Creating a placeholder with zeros. 
    merged_array = (left_array_length + right_array_length) * [0]
    
    left_index = 0
    right_index = 0
    current_index = 0
    while left_index < left_array_length or right_index < right_array_length:
        # merging by sorting.
        if left_index < left_array_length and right_index < right_array_length:
            if left_array[left_index] > right_array[right_index]:
                merged_array[current_index] = right_array[right_index]
                right_index += 1
            elif left_array[left_index] <= right_array[right_index]:
                merged_array[current_index] = left_array[left_index]
                left_index += 1
        else:
            # Left over elements.
            if left_index < left_array_length:
                merged_array[current_index:] = left_array[left_index:]
                current_index += len(left_array[left_index:])
                left_index = left_array_length
            elif right_index < right_array_length:
                merged_array[current_index:] = right_array[right_index:]
                current_index += len(right_array[right_index:])
                right_index = right_array_length

        current_index += 1
    return merged_array


def merge_sort(array):
    """Recursive merge sort implementation"""
    length_of_the_array = len(array)
    # If length of the array is not 2 or more, no need to sort, just pass along.
    if length_of_the_array <= 1:
        return array

    left_array = array[:length_of_the_array//2]
    right_array = array[length_of_the_array//2:]
    merged_left = merge_sort(left_array)
    merge_right = merge_sort(right_array)
    merged_array = _sort_and_merge_sub_arrays(merged_left, merge_right)
    return merged_array


if __name__ == "__main__":
    array = [2, 1, 5, 3, 4, 2, 10, -1]
    assert (bubble_sort(array) == [-1, 1, 2, 2, 3, 4, 5, 10])
    assert (merge_sort(array) == [-1, 1, 2, 2, 3, 4, 5, 10])


