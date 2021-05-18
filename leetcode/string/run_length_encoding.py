"""Input  :  str = 'wwwwaaadexxxxxx'
Output : 'w4a3d1e1x6'"""


def run_length_encoding(input_string):
    """Just an iterative solution to the run-length encoding problem"""
    char_count = 0
    previous_character = None
    encoding = str()
    for char_num in range(len(input_string)):
        current_character = input_string[char_num]
        if previous_character is None:
            char_count = 1
            previous_character = current_character
            continue

        if previous_character == current_character:
            char_count += 1
        else:
            encoding += previous_character
            encoding += str(char_count)
            char_count = 1
            previous_character = current_character

    # The final character gets missed.
    if char_count > 0:
        encoding += previous_character
        encoding += str(char_count)
    return encoding


if __name__ == "__main__":
    online_eg = 'wwwwaaadexxxxxx'
    solution = run_length_encoding(online_eg)
    print(solution)
    expected_solution = 'w4a3d1e1x6'
    assert solution == expected_solution
