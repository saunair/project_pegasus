

# This is very close to a binary tree, the frequency being the occurences count 
class Node:
    """

    Parameters
    ----------
    frequency: int 
        The occrance count
    left: Node | None
        The left daughter node
    right: Node | None
        The right daughter node
    character: str
        The character repr of the node, none if just a parent for connection
    huff_code: bool
        the huffman direction of the character represented by this node.

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


def get_str_forest(input_string):
    """Get unique chars and their occurences in the string, then generate a forest of nodes out of it.
    
    Parameters
    ----------
    input_string: str
        The string that needs to be compressed.

    Returns
    -------
    list: list of nodes representing each character.

    """
    all_char_counts = {}
    for char in input_string:
        if char in all_char_counts:
            all_char_counts[char] += 1
        else:
            all_char_counts[char] = 1

    forest = []
    for char, occurance in all_char_counts.items():
        forest.append(Node(frequency=occurance, character=char))
    return forest


def _get_str_ip():
    """Just a user mock string."""
    return "I am the stupidest living being in the entire universe, and I still somehow find a lot of folks who are just stupider."


def print_tree(node, parent_huff=None, huffman_info=None):
    """Print the huffman codes by parsing the whole tree
    
    Parameters
    ----------
    node: Node
        The root of the tree that needs to be printed.
    parent_huff: str | None
        Huffman code of the parent of the node.
    huffman_info: {} | None
        Tracking mutable to carry the huffman codes through the traversal.

    Returns
    -------
    dict: the huffman info with keys as characters and values as the code.

    """
    if huffman_info is None:
        huffman_info = dict()

    if parent_huff is not None:
        current_huffman = parent_huff + f"{node.huff_code}"
    else: 
        current_huffman = f"{node.huff_code}"

    if node.left is not None:
        print_tree(
            node=node.left, 
            parent_huff=current_huffman, 
            huffman_info=huffman_info
        )
    if node.right is not None:
        print_tree(
            node=node.right, 
            parent_huff=current_huffman, 
            huffman_info=huffman_info
        )

    if node.character is not None:
        huffman_info[node.character] = current_huffman
    return huffman_info


def build_huffman_tree(forest):
    """Build the huffman tree from the forest. 
    Return the root node that represents the whole heap under it.

    Parameters
    ----------
    forest : list[Node]
        Nodes representing each character. Doesn't have to be sorted by frequency.

    Returns
    -------
    Node: The root node of the huffman tree.

    """
    daughter_node = None

    # forest is a priority queue used to populate the heap.
    while len(forest) > 1:
        # Sort the tree by frequency.
        forest = sorted(forest, key=lambda x: x.frequency)

        # Create a mini-tree with the lowest frequency nodes
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

    # We exit the loop only when there is one Node left, which is the root node.
    forest[0].huff_code = 0
    return forest[0]


if __name__ == "__main__":
    input_string = _get_str_ip()
    forest = get_str_forest(input_string)
    tree_root = build_huffman_tree(forest)
    huffman_codes = print_tree(tree_root)
    print(huffman_codes)
