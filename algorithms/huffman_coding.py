

# This is very close to a binary tree, the frequency being the occurences count 
class Node:
    """

    Parameters
    ----------
    frequency: int 
        The occrance count
    left: The left daughter node
    right: The right daughter node
    character: The character repr of the node, none if just a parent for connection

    """
    def __init__(self, frequency, left=None, right=None, character=None, huff_code=None):
        self.__frequency = frequency
        self.__left = left
        self.__right = right
        self.__character = character
        self.__huff_code = huff_code
        if self.__left is not None:
            assert self.left.frequency + self.right.frequency == self.frequency
    
    def __repr__(self):
        return f"huff_code: {self.huff_code}, frequency: {self.frequency}, character: {self.character}"

    @property
    def left(self):
        return self.__left
    
    @property
    def frequency(self):
        return self.__frequency

    @property
    def right(self):
        return self.__right

    @property
    def character(self):
        return self.__character

    @property
    def huff_code(self):
        return self.__huff_code

    @huff_code.setter
    def huff_code(self, huff_code):
        self.__huff_code = huff_code


def get_str_sets(input_string):
    """Get unique chars and their occurences in the string.
    
    Parameters
    ----------
    input_string: str

    Returns
    -------
    dict: keys as characters and the frequencys as their count

    """
    all_char_counts = {}
    for char in input_string:
        if char in all_char_counts:
            all_char_counts[char] += 1
        else:
            all_char_counts[char] = 1

    sorted_dict = {k: v for k, v in sorted(all_char_counts.items(), key=lambda x: x[1], reverse=False)}
    return sorted_dict


def get_str_ip():
    return "I am the stupidest living being in the entire universe, and I still somehow find a lot of folks who are just stupider."


def create_forest(sorted_dict):
    forest = []
    for char, occurance in sorted_dict.items():
        forest.append(Node(frequency=occurance, character=char))
    return forest


def print_tree(node, parent_huff=""):
    """Print the huffman codes by parsing the whole tree"""
    if parent_huff is not None:
        current_huffman = parent_huff + f"{node.huff_code}"
    else: 
        current_huffman = f"{node.huff_code}"

    if node.left is not None:
        print_tree(node.left, current_huffman)
    if node.right is not None:
        print_tree(node.right, current_huffman)

    if node.character is not None:
        print(f"{node.character}: {current_huffman}")


def build_huffman_tree(sorted_dict):
    daughter_node = None
    forest = create_forest(sorted_dict)
    while len(forest) > 1:
        forest = sorted(forest, key=lambda x: x.frequency)
        left_node = forest[0]
        right_node = forest[1]
        left_node.huff_code = 0 
        right_node.huff_code = 1
        current_node = Node(
            left=left_node, 
            right=right_node, 
            frequency=left_node.frequency + right_node.frequency, 
        )
        forest.remove(left_node)
        forest.remove(right_node)
        forest.append(current_node)
    return forest[0]


if __name__ == "__main__":
    input_string = get_str_ip()
    sorted_dict = get_str_sets(input_string)
    tree_root = build_huffman_tree(sorted_dict)
    print_tree(tree_root, None)
