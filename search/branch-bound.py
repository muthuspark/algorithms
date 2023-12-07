# **************************************
# Solve the knapsack problem using the Branch and Bound
#         algorithm.
# **************************************
import heapq


class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        # if weight is 0, value_to_weight is also 0
        self.value_to_weight = value / weight if weight != 0 else 0


class TreeNode:
    def __init__(self, level, included_indexes):
        self.level = level
        self.included_indexes = included_indexes
        self.priority = 0
        self.upper_bound = 0
        self.total_weight = 0
        self.total_value = 0

    def __lt__(self, other):
        return self.priority < other.priority


class BranchAndBoundSolver:
    def __init__(self, knapsack_capacity, items):
        """
        Initialize the BranchAndBoundSolver.

        Args:
            max_weight (int): The maximum weight the knapsack can hold.
            items (list): The list of items to consider for the
            knapsack problem.
        """
        self.knapsack_capacity = knapsack_capacity
        # Sort the items based on their value-to-weight ratio in
        # descending order
        # Sorting items by value-to-weight ratio allows for a greedy
        # approach, where you consider adding items to the knapsack in
        # descending order of their value-to-weight ratio. This means you
        # prioritize items that give you the most value for
        # the least weight.
        self.items = sorted(
            items, key=lambda el: el.value_to_weight, reverse=True)

        self.items.insert(0, Item("0", 0, 0))
        self.best_profit = 0
        self.best_combination = []

    def build_tree_node(self, level, included_indexes):
        node = TreeNode(level, list(set(included_indexes)))
        node.total_weight = self.total_weight_of(included_indexes)
        node.total_value = self.total_value_of(included_indexes)
        node.upper_bound = self.get_upper_bound(node)
        # Priority of a node to be picked is decided by the
        # upper bound of the current set of element in this
        # branch. -1 is multiplied here is to pick the largest from the
        # priority queue
        node.priority = -1 * node.upper_bound
        return node

    def total_weight_of(self, included_indexes):
        return sum(
            self.items[index].weight
            for index in included_indexes
            if index < len(self.items) - 1
        )

    def total_value_of(self, included_indexes):
        return sum(
            self.items[index].value
            for index in included_indexes
            if index < len(self.items) - 1
        )

    def solve(self):
        """
        Solve the knapsack problem using the Branch and Bound
        algorithm.

        Returns:
            list: The best solution found for the knapsack problem.
        """
        priority_queue = []
        # First an empty/dummy node
        start_node = self.build_tree_node(0, [])
        heapq.heappush(priority_queue, start_node)

        while priority_queue:
            current_node = heapq.heappop(priority_queue)

            # Get out of this loop if reached limit of
            # elements in terms of tree levels.
            if current_node.level == len(self.items) - 1:
                break

            if self.is_infeasible(current_node):
                continue

            print(f"upper_bound:{current_node.upper_bound}")
            print(f"items:{current_node.included_indexes}")
            print(f"profit:{current_node.total_value}")
            print(f"weight:{current_node.total_weight}")
            print(f"best profit:{self.best_profit}")

            # if the total value of items added till now exceeds the tracked
            # best profit then update the optimal best
            # solution
            if current_node.total_value > self.best_profit:
                self.best_profit = current_node.total_value
                self.best_combination = current_node

            print("\n")
            next_level = current_node.level + 1

            left_node = self.build_tree_node(
                next_level, current_node.included_indexes + [next_level]
            )
            heapq.heappush(priority_queue, left_node)

            right_node = self.build_tree_node(
                next_level, current_node.included_indexes)
            heapq.heappush(priority_queue, right_node)

        return self.get_best_solution()

    def get_upper_bound(self, node):
        """
        Calculate the upper bound of a given node.

        Args:
            node (TreeNode): The node for which to
            calculate the upper bound.

        Returns:
            int: The upper bound of the node.
        """
        value = self.total_value_of(node.included_indexes)
        weight = self.total_weight_of(node.included_indexes)

        if node.level == len(self.items) - 1:
            # this means we just encountered an end node, so we add a zero
            # value item to stop further deep processing.
            next_element = Item("END", 0, 0)
        else:
            next_element = self.items[node.level + 1]
        bound = value + (self.knapsack_capacity - weight) * \
            next_element.value_to_weight
        return bound

    def is_infeasible(self, node):
        # If the upper bound of the current node is less than our best profit
        # or if the total weight included till now is greater than the
        # allowed maximum weight then discard this
        # branch
        return (
            node.upper_bound < self.best_profit
            or node.total_weight > self.knapsack_capacity
        )

    def get_best_solution(self):
        return self.best_profit

    def included_items(self):
        return [self.items[i] for i in self.best_combination.included_indexes]


# Example usage
# capacity = 50
# items = [Item('P1', 50, 10), Item('P2', 98, 5), Item('P3', 54, 4), Item('P4', 6, 20), Item('P5', 34, 9), Item('P6', 66, 18), Item('P7', 63, 20), Item(
#     'P8', 52, 5), Item('P9', 39, 10), Item('P10', 62, 4), Item('P11', 46, 3), Item('P12', 75, 11), Item('P13', 28, 16), Item('P14', 65, 18), Item('P15', 18, 4)]

capacity = 15
items = [
    Item("P1", 4, 12),
    Item("P2", 2, 2),
    Item("P3", 10, 4),
    Item("P4", 1, 1),
    Item("P5", 2, 1),
]

solver = BranchAndBoundSolver(knapsack_capacity=capacity, items=items)
print("Maximum Profit:", solver.solve())
print("Included Items")
for item in solver.included_items():
    print(f"Product {item.name}: profit= {item.value}, weight={item.weight}")
