# Maximum number of nodes at level "l" is 2^l. Level of the root is 0.


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right 
    
    @classmethod
    def make_tree_from_sorted_list(cls, sorted_list):
        """Make tree recursively from the sorted-list."""
        if len(sorted_list) == 1:
            return cls(data=sorted_list[0])

        elif len(sorted_list) == 0:
            return cls(data=None)

        mid_val = int(len(sorted_list) / 2)
        node = cls(data=sorted_list[mid_val])
        node.left = cls.make_tree_from_sorted_list(sorted_list[:mid_val])
        node.right = cls.make_tree_from_sorted_list(sorted_list[mid_val + 1:])
        return node
    
    def insert(self, data):
        assert isinstance(data, float), f"Data to be inserted has to be a {float} not {type(data)}"
        if self.data is None:
            self.data = data
            return

        if data > self.data:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data=data)
            return

        assert data <= self.data
        if self.left is not None:
            self.left.insert(data)
            return

        self.left = Node(data=data)
        return 

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(f" {self.data}")
        if self.right:
            self.right.print_tree()

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

    @property
    def max_depth(self):
        """Assumig a balanced tree here"""
        if self.data is None:
            return 0

        if self.left is not None and self.right is not None:
            child_depth = max(self.left.max_depth, self.right.max_depth)
            return child_depth + 1

        # left or right is not None, just one of the lengths left.
        return 1


# Minor test script
left_node = Node(1, None, None)
right_node = Node(3, None, None)
root_node = Node(2, left=left_node, right=right_node)

assert root_node.max_depth == 2


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

root_node.print_tree()
assert root_node.max_depth == 3

example_sorted_list = [float(num) for num in range(30)]

root_node = Node.make_tree_from_sorted_list(example_sorted_list)
import IPython; IPython.embed()
print(root_node.print_tree())

