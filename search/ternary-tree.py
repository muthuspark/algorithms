class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.mid = None
        self.flag = False  # Marks the end of a string

def insert_node(root, string, index):
    if not root:
        root = Node(string[index])  # Allocate memory for a new node

    if index < len(string) - 1:
        if string[index] < root.key:  # If the current character is smaller
            root.left = insert_node(root.left, string, index)
        elif string[index] > root.key:  # If the current character is greater
            root.right = insert_node(root.right, string, index)
        else:
            root.mid = insert_node(root.mid, string, index + 1)  # If the current character is equal
    else:
        root.flag = True  # Mark the node as the end of the string

    return root

def build_tree(strings):
    root = None
    for string in strings:
        root = insert_node(root, string, 0)
    return root

def search(root, string):
    previous = root
    for char in string:
        while root and root.key != char:  # Search for the appropriate node
            previous = root
            root = char < root.key and root.left or root.right

        if root:  # If the character matches, follow the mid link
            previous = root
            root = root.mid
        else:
            return False

    return previous.flag  # If the node is marked, the string is found

if __name__ == "__main__":

    strings = ['she', 'sells', 'sea', 'shells', 'at', 'the', 'sea', 'shore']

    root = build_tree(strings)

    input_string = "as"
    if search(root, input_string):
        print("String Found!")
    else:
        print("String Not Found!")