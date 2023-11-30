import random
import math


class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def get_next_player(self, current_player):
        return 'O' if current_player == 'X' else 'X'

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = self.get_next_player(self.current_player)
            return True
        return False

    def location_empty(self, row, col):
        return self.board[row][col] == " "

    def is_valid_move(self, row, col):
        valid_row = 0 <= row < 3
        valid_col = 0 <= col < 3
        return (valid_row and valid_col and 
                        self.location_empty(row, col))

    def is_game_over(self):
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != " ":
                return True
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == 
                    self.board[2][col] != " "):
                return True
        if (self.board[0][0] == self.board[1][1] == 
                    self.board[2][2] != " "):
            return True
        if (self.board[0][2] == self.board[1][1] == 
                    self.board[2][0] != " "):
            return True
        if all(cell != " " for row in self.board for cell in row):
            return True
        return False

    def get_winner(self):
        # Check rows for a winner
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != " ":
                return row[0]
        
        # Check columns for a winner
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == 
                    self.board[2][col] != " "):
                return self.board[0][col]
        
        # Check diagonals for a winner
        if (self.board[0][0] == self.board[1][1] == 
                    self.board[2][2] != " "):
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] == 
                    self.board[2][0] != " "):
            return self.board[0][2]
        
        return None


class MCTSTreeNode:
    def __init__(self, state):
        self.state = state
        self.children = []
        self.parent = None
        self.visits = 0
        self.value = 0


def select(node):
    while not node.state.is_game_over():
        if len(node.children) < len(node.state.board) * len(node.state.board[0]):
            return expand(node)
        else:
            node = best_child(node)
    return node


def expand(node):
    unexplored_moves = [
        (row, col)
        for row in range(3)
        for col in range(3)
        if node.state.is_valid_move(row, col)
    ]
    row, col = random.choice(unexplored_moves)
    new_state = TicTacToe()
    new_state.board = [row.copy() for row in node.state.board]
    new_state.current_player = node.state.current_player
    new_state.make_move(row, col)
    child_node = MCTSTreeNode(new_state)
    child_node.parent = node
    node.children.append(child_node)
    return child_node


def best_child(node):
    # You can adjust this parameter for exploration-exploitation trade-off
    exploration_weight = 1.0
    best_child_node = None
    best_child_value = float("-inf")
    for child in node.children:
        child_value = (child.value / child.visits) + exploration_weight * (
            math.sqrt(2 * math.log(node.visits) / child.visits)
        )
        if child_value > best_child_value:
            best_child_value = child_value
            best_child_node = child
    return best_child_node


def simulate_random_game(state):
    while not state.is_game_over():
        available_moves = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if state.is_valid_move(row, col)
        ]
        random_move = random.choice(available_moves)
        state.make_move(random_move[0], random_move[1])
    return state.get_winner()


def backpropagate(node, winner):
    while node is not None:
        node.visits += 1
        if node.state.current_player == winner:
            node.value += 1
        node = node.parent


num_simulations = 1000  # You can adjust the number of simulations
ttt = TicTacToe()


def get_next_move(ttt):
    root = MCTSTreeNode(ttt)
    for _ in range(num_simulations):
        selected_node = select(root)
        winner = simulate_random_game(selected_node.state)
        backpropagate(selected_node, winner)

    # Choose the best move based on the most visited child
    best_child = max(root.children, key=lambda child: child.visits)
    best_move = None
    for row in range(3):
        for col in range(3):
            if root.state.board[row][col] != best_child.state.board[row][col]:
                best_move = (row, col)
    print("Best Move:", best_move)
    return best_move


def play(current_player):
    if not ttt.get_winner():
        ttt.current_player = current_player
        best_move = get_next_move(ttt)
        ttt.make_move(best_move[0], best_move[1])
        ttt.display_board()


ttt.display_board()
play("X")
play("O")
play("X")
play("O")
play("X")
play("O")
play("X")
play("O")
play("X")
