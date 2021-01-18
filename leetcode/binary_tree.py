# Maximum number of nodes at level "l" is 2^l. Level of the root is 0.


class Node:
    def __init__(self, data, left, right):
        self.__data = data
        self.__left = left
        self.__right = right 

    @property
    def data(self):
        return self.__data

    @property
    def right(self):
        return self.__right
    
    @property
    def left(self):
        return self.__left
    
    @right.setter
    def right(self, node):
        assert isinstance(node, Node) or isinstance(node, None)
        self.__right = node
    
    @left.setter
    def left(self, node):
        assert isinstance(node, Node) or isinstance(node, None)
        self.__left = node
    
    @data.setter
    def data(self, data):
        assert isinstance(data, float) or isinstance(data, None)
        self.__data = data


def get_max_depth(node):
    """Assumig a balanced tree here"""
    if node.data is None:
        return 0

    if node.left is not None and node.right is not None:
        child_depth = max(get_max_depth(node.left), get_max_depth(node.right))
        return child_depth + 1

    # left or right is not None, just one of the lengths left.
    return 1


# Minor test script
left_node = Node(1, None, None)
right_node = Node(3, None, None)
root_node = Node(2, left=left_node, right=right_node)

assert get_max_depth(root_node) == 2


""" Current tree:

      5
    /   \
   3     7
  / \   / \
 1   4 6  none
  
"""
left_node = Node(3, None, None)
right_node = Node(7, None, None)
root_node = Node(5, left=left_node, right=right_node)
left_node.left = Node(1, None, None)
left_node.right = Node(4, None, None)

right_node.left = Node(6, None, None)

assert get_max_depth(root_node) == 3
