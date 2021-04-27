
UNIT_STRING = "neigh"

def _next_expected_char(current_count):
    if current_count == len(UNIT_STRING):
        idx = 0
    else:
        idx = current_count + 1
    return UNIT_STRING[idx]


def count_horses_from_string(recording: str) -> int:
    pool_of_horse_counts = [0] # assume there is atleast one horse
    char_list = list(UNIT_STRING)
    current_str_count = 0

    def _update_pool_of_horses(pool_of_horse_counts, current_horse_index):
        count = 0
        while count < len(pool_of_horse_counts):
            if pool_of_horse_counts[count] != 0 or (count == current_horse_index):
                pool_of_horse_counts[count] += 1

            if pool_of_horse_counts[count] == len(char_list):
                # Resetting the count as the string is complete.
                pool_of_horse_counts[count] = 0
            count += 1

    current_horse_index = 0
    while current_str_count < len(recording):
        current_char = recording[current_str_count]
        if current_char not in char_list:
            raise ValueError(f"Input recording contained an unknown character {current_char} which isn't from {UNIT_STRING}")

        if current_char != UNIT_STRING[pool_of_horse_counts[current_horse_index]]:
            # Unexpected char for current horse, should be first char!
            assert current_char == UNIT_STRING[0]
            if 0 in pool_of_horse_counts:
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
