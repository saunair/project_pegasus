from copy import copy

from dataclasses import dataclass
import numpy as np


OPERATOR_IMPORTANCE = ['^', '/', '*', '+', '-']
NUMBERS = range(10)


@dataclass(frozen=True, init=True)
class SingleStack:
    operand_list : list
    operator_list : list


def get_operators_and_operands_from_string(user_string):
    """Convert the input string to operators and operands.

    Parameters
    ----------
    user_string : str
        the bodmas string

    Returns
    -------
    [SingleStack]

    Raises
    ------
    ValueError : If an unsupported character is encountered in `user_string`.

    """

    operator_list = []
    operand_list = []
    num_cache = 0.
    decimal_multiplier = 1.
    user_input = list(user_string)  # this makes a copy too
    for char_index, character in enumerate(user_input):
        print(user_input)
        if character == " ":
            continue 
        
        elif character == '(':
            index_to_expr = user_input[char_index:].index(')')
            if index_to_expr < 0:
                raise ValueError("invalid expression as it has a wrong bracket structure.")
            internal_soln = solve_bracket(
                get_operators_and_operands_from_string(
                    user_input[char_index+1:char_index+index_to_expr]
                )
            )
            del user_input[char_index + 1: char_index+index_to_expr + 1]
 
            user_input[char_index] = internal_soln
            num_cache = internal_soln
            continue

        elif character == '.':
            decimal_multiplier /= 10.

        elif character in OPERATOR_IMPORTANCE:
            operator_list.append(character)
            operand_list.append(num_cache)
            num_cache = 0.0
            decimal_multiplier = 1.
        
        elif int(character) in NUMBERS:
            current_digit = int(character) 
            # If we encontered a `.` in the past, we need to keep dividing by 10.
            current_digit *= decimal_multiplier
            # If we never encountered a `.`, the older number in the cache needs to be multiplied by 10.
            num_cache = num_cache*(1.0 if decimal_multiplier < 1.0 else 10.0) + current_digit

            if decimal_multiplier < 1.0:
                decimal_multiplier /= 10.

        else:
            raise ValueError(f"Unsupported character {character} in the equation.")

    operand_list.append(num_cache)         
    
    return SingleStack(operator_list=operator_list, operand_list=operand_list)


def solve_bracket(single_bodmas_stack):
    """

    Parameters
    ----------
    [SingleStack], [char]

    Returns
    -------
    float : answer to the calculation.

    """
    number_stack = copy(single_bodmas_stack.operand_list)
    operator_stack = copy(single_bodmas_stack.operator_list)
    operand_imp = copy(OPERATOR_IMPORTANCE)
    operation = {
       '*': lambda x,y: x * y, 
       '+': lambda x,y: x + y, 
       '-': lambda x,y: x - y, 
       '/': lambda x,y: x / y, 
       '^': lambda x,y: x ** y, 
    }

    while len(number_stack) > 0 and len(operand_imp) > 0:
        current_operator = operand_imp[0]
        for index, operator in enumerate(operator_stack):
            if operator == current_operator:
                ans = operation[current_operator](
                    number_stack[index], 
                    number_stack[index + 1]
                )
                number_stack[index] = ans
                del number_stack[index + 1]
                del operator_stack[index] 
        if current_operator not in operator_stack:
            del operand_imp[0]
    return number_stack[0]
                

if __name__ == "__main__":
    a = get_operators_and_operands_from_string("3.2-20+4/10+92*100")
    soln = solve_bracket(a)
    assert np.isclose(soln, -9217.1999, rtol=1e-3), f"got {soln} not 1996.8"
    soln = solve_bracket(get_operators_and_operands_from_string("2^3+2"))
    assert soln == 10.0, f"got {a} instead of 10.0"
    
    a = get_operators_and_operands_from_string("3.2-(20+4)/10+92*100")
    soln = solve_bracket(a)
    assert np.isclose(soln, -9199.1999, rtol=1e-4), f"not {soln}"
    
    soln = solve_bracket(get_operators_and_operands_from_string("(2^3)"))
    assert soln == 8, f"need 8 not {soln}"
    
    soln = solve_bracket(get_operators_and_operands_from_string("(2*2)+4"))
    assert soln == 8, f"need 1 not {soln}"
    
    soln = solve_bracket(get_operators_and_operands_from_string("(2*2+2)+4"))
    assert soln == 10, f"need 24 not {soln}"
