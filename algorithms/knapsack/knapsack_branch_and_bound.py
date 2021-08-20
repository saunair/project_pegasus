"""Knapsack solution using the branch and bound method."""

class Item:
    """Representation of one item from the total set of objects that can be chosen."""
    def __init__(self, weight: int, value: int):
        # Todo: Make this a dataclass.
        self.__weight = weight
        self.__value = value

    def __repr__(self):
        return f"weight: {self.weight}, value:{self.value}, ratio:{self.ratio}"
    
    @property
    def value(self):
        return self.__value
    
    @property
    def weight(self):
        return self.__weight
    
    #@weight.setter
    #def weight(self, w):
    #    self.__weight = w

    #@value.setter
    #def value(self, v):
    #    self.__value = v

    @property
    def ratio(self):
        return self.value / self.weight
    
    def __ge__(self, other):
        if self.ratio >= other.ratio:
            return True
        if self.ratio < other.ratio:
            return False


class Node: 
    """Node of the branch and bound tree."""
    def __init__(self, level: int = None, profit: int = None, bound: float = None, weight: float = None):
        # TODO: make this a Dataclass.
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight


def bound(node_u: Node, total_knapsack_weight: int, item_value_pairs: list) -> int:
    # If the node's weight exceeds the capacity, return a zero value as (an early exit) solution.
    if node_u.weight >= total_knapsack_weight:
        return 0

    profit_bound = node_u.profit
    total_weight = node_u.weight
    item_number = node_u.level + 1

    while item_number < len(item_value_pairs) and total_weight + item_value_pairs[item_number].weight <= total_knapsack_weight:
        total_weight += item_value_pairs[item_number].weight
        profit_bound += item_value_pairs[item_number].value
        item_number += 1

    if item_number < len(item_value_pairs):
        profit_bound += (total_knapsack_weight - total_weight) * item_value_pairs[item_number].ratio

    return profit_bound


def knapsack_bb(total_knapsack_weight: int, item_value_pairs: list):
    """Knapsack using greedy branch and bound."""
    def _item_ratio(item):
        return item.ratio

    item_value_pairs.sort(key=_item_ratio, reverse=True)
    print(item_value_pairs)

    current_queue = []
    u, v = Node(level=-1, profit=0, weight=0), Node(level=-1, profit=0, weight=0)
    current_queue.append(u)
    max_profit = 0

    while len(current_queue) > 0:
        u = current_queue.pop(-1)
        if u.level == -1:
            v.level = 0
        
        # This condition? 
        if u.level == len(item_value_pairs) - 1:
            continue

        v.level = u.level + 1
        v.weight = u.weight + item_value_pairs[v.level].weight;
        v.profit = u.profit + item_value_pairs[v.level].value;

        # If cumulated weight is less than W and profit is greater than previous profit, update max_profit.
        if v.weight <= total_knapsack_weight and v.profit > max_profit:
            max_profit = v.profit

        v.bound = bound(v, total_knapsack_weight, item_value_pairs)
        if v.bound > max_profit:
            current_queue.append(v)

        # Do the same thing, but without taking the item in knapsack.
        v.weight = u.weight;
        v.profit = u.profit;
        v.bound = bound(v, total_knapsack_weight, item_value_pairs);
        if v.bound > max_profit:
            current_queue.append(v)

    return max_profit


if __name__ == "__main__":
    W = 95
    item_value_pairs = [(2, 40), (3.14, 50), (1.98, 100), (5, 95), (3, 30)]
    item_value_pairs = [Item(weight=weight, value=value) for value, weight in item_value_pairs]
    print(
        knapsack_bb(
            total_knapsack_weight=W, 
            item_value_pairs=item_value_pairs,
        )
    )
