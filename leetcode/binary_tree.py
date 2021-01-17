
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
    def set_right(self, node):
        assert isinstance(Node, node) or isinstance(Node, None)
        self.__right = node
    
    @left.setter
    def set_left(self, node):
        assert isinstance(Node, node) or isinstance(Node, None)
        self.__left = node
    
    @data.setter
    def set_data(self, data):
        assert isinstance(data, float)
        self.__data = data


# Minor test script
left_node = Node(1, None, None)
right_node = Node(3, None, None)
root_node = Node(2, left=left_node, right=right_node)
