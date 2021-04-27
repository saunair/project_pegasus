
UNIT_STRING = "neigh"

def count_horses_from_string(recording: str) -> int:
    """Count minimum number of string generators in the scene"""
    pool_of_horse_counts = [0] # assume there is atleast one horse
    char_list = list(UNIT_STRING)
    current_str_count = 0

    def _update_pool_of_horses(pool_of_horse_counts: List[int], current_horse_index: int):
        """Update the expected index count of every word"""
        count = 0
        # Go through every horse and update its count.
        while count < len(pool_of_horse_counts):
            # If the horse count is zero no need to update, unless it is the current horse that is neighing.
            if pool_of_horse_counts[count] != 0 or (count == current_horse_index):
                pool_of_horse_counts[count] += 1

            # If the word has reached its end, we need to reset the char index count.
            if pool_of_horse_counts[count] == len(char_list):
                # Resetting the count as the string is complete.
                pool_of_horse_counts[count] = 0
            count += 1

    current_horse_index = 0
    while current_str_count < len(recording):
        current_char = recording[current_str_count]
        if current_char not in char_list:
            raise ValueError(f"Input recording contained an unknown character {current_char} which isn't from {UNIT_STRING}")

        # Check if it is an interruption from the current word
        if current_char != UNIT_STRING[pool_of_horse_counts[current_horse_index]]:
            assert current_char == UNIT_STRING[0]
            if 0 in pool_of_horse_counts: # One of the horses in the list already neighed. So It is probably the same horse that has interrupted. 
                current_horse_index = pool_of_horse_counts.index(0)
            else:
                pool_of_horse_counts.append(0)
                current_horse_index = len(pool_of_horse_counts) - 1
        _update_pool_of_horses(pool_of_horse_counts, current_horse_index)

        current_str_count += 1

    return len(pool_of_horse_counts)
        


if __name__ == "__main__":
    case1 = "neigh" # one horse
    assert count_horses_from_string(case1) == 1
    case2 = "neighneigh" # one horses
    assert count_horses_from_string(case2) == 1
    case3 = "neigneigh" # two horses
    assert count_horses_from_string(case3) == 2
    case4 = "neigneigneigh" # still two horses
    assert count_horses_from_string(case4) == 2
    case5 = "neneneigh" # three horses
    assert count_horses_from_string(case5) == 3
    case6 = "neigneigneigh" # two horses
    assert count_horses_from_string(case6) == 2
