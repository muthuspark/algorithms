class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        
        self.value_to_weight = value / weight if weight != 0 else 0


class TreeNode:
    def __init__(self, level, included_items_indexes):
        self.level = level
        self.included_items_indexes = included_items_indexes


class BranchAndBoundSolver:
    def __init__(self, max_weight, items):
        """
        Initialize the BranchAndBoundSolver.

        Args:
            max_weight (int): The maximum weight the knapsack can hold.
            items (list): The list of items to consider for the knapsack problem.
        """
        self.max_weight = max_weight
        # Sort the items based on their value-to-weight ratio in descending order
        # Sorting items by value-to-weight ratio allows for a greedy
        # approach, where you consider adding items to the knapsack in
        # descending order of their value-to-weight ratio. This means you
        # prioritize items that give you the most value for the least weight.
        self.items = sorted(
            items, key=lambda el: el.value_to_weight, reverse=True)
        self.items.insert(0, Item('0', 0, 0))
        self.best_profit = 0
        self.possible_solutions = []

    def solve(self):
        """
        Solve the knapsack problem using the Branch and Bound algorithm.

        Returns:
            list: The best solution found for the knapsack problem.
        """
        def recursion_step(current_root):
            if self.get_upper_bound(current_root) < self.best_profit or self.is_infeasible(current_root):
                return

            current_node_profit = sum(
                (self.items[i].value for i in current_root.included_items_indexes))
            if current_node_profit > self.best_profit:
                self.best_profit = current_node_profit

            if current_root.level == len(self.items) - 1:
                self.possible_solutions.append(current_root)
                return

            left_node = TreeNode(current_root.level + 1,
                                 current_root.included_items_indexes + [current_root.level + 1])

            right_node = TreeNode(current_root.level + 1,
                                  current_root.included_items_indexes[:])

            recursion_step(left_node)
            recursion_step(right_node)

        dummy_node = TreeNode(0, [])
        recursion_step(dummy_node)

        return self.get_best_solution()

    def get_upper_bound(self, node):
        """
        Calculate the upper bound of a given node.

        Args:
            node (TreeNode): The node for which to calculate the upper bound.

        Returns:
            int: The upper bound of the node.
        """
        value = sum((self.items[i].value for i in node.included_items_indexes))
        weight = sum(
            (self.items[i].weight for i in node.included_items_indexes))

        if node.level == len(self.items) - 1:
            next_element = Item('0', 0, 0)
        else:
            next_element = self.items[node.level + 1]
        return value + (self.max_weight - weight) * next_element.value_to_weight

    def is_infeasible(self, node):
        # Check if the total weight of the included items exceeds the maximum weight
        return sum((self.items[i].weight for i in node.included_items_indexes)) > self.max_weight

    def get_best_solution(self):
        if not self.possible_solutions:
            return None

        values = [sum((self.items[i].value for i in node.included_items_indexes))
                  for node in self.possible_solutions]
        return max(values)

    def included_items(self):
        included = []
        for node in self.possible_solutions:
            for i in node.included_items_indexes:
                included.append(self.items[i])
        return included


# Example usage
capacity = 50
items = [Item('P1', 50, 10), Item('P2', 98, 5), Item('P3', 54, 4), Item('P4', 6, 20), Item('P5', 34, 9), Item('P6', 66, 18), Item('P7', 63, 20), Item(
    'P8', 52, 5), Item('P9', 39, 10), Item('P10', 62, 4), Item('P11', 46, 3), Item('P12', 75, 11), Item('P13', 28, 16), Item('P14', 65, 18), Item('P15', 18, 4)]

# capacity = 15
# items = [Item('P1', 4, 12), Item('P2', 2, 2), Item('P3', 10, 4), Item('P4', 1, 1), Item('P5', 2, 1)]

solver = BranchAndBoundSolver(max_weight=capacity, items=items)
print("Maximum Profit:", solver.solve())
print("Selected Items")
for item in solver.included_items():
    print(f"Product {item.name}: profit= {item.value}, weight={item.weight}")
