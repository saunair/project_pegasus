from copy import copy


def get_largest_divisible_subset(input_numbers: list):
    sorted_numbers = copy(input_numbers)
    sorted_numbers.sort()
    divisible_numbers = len(sorted_numbers)*[1]
    max_index = 0
    previous_divisible_index = len(sorted_numbers)*[-1]
    for index in range(len(sorted_numbers)):
        for lower_index in range(index):
            if sorted_numbers[index] % sorted_numbers[lower_index] == 0:
                if divisible_numbers[lower_index] + 1 > divisible_numbers[index]:
                    divisible_numbers[index] = divisible_numbers[lower_index] + 1
                    previous_divisible_index[index] = lower_index
        if divisible_numbers[index] > divisible_numbers[max_index]:
            max_index = index
    
    largest_subset = []
    while True:
        largest_subset.append(sorted_numbers[max_index])
        if previous_divisible_index[max_index] != -1:
            max_index = previous_divisible_index[max_index]
        else:
            break
    return largest_subset


if __name__ == "__main__":
    input_numbers = [16, 7, 4, 6, 8, 3]
    print(get_largest_divisible_subset(input_numbers))
    input_numbers = [16] 
    print(get_largest_divisible_subset(input_numbers))
    input_numbers = [] 
    print(get_largest_divisible_subset(input_numbers))
