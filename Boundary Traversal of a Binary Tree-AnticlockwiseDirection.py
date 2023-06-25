# Definition of a binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform boundary traversal
def boundary_traversal(root):
    if root:
        print(root.data, end=" ")  # Print root node

        # Traverse left boundary (excluding leaf nodes)
        traverse_left_boundary(root.left)

        # Traverse leaf nodes
        traverse_leaves(root.left)
        traverse_leaves(root.right)

        # Traverse right boundary (excluding leaf nodes)
        traverse_right_boundary(root.right)

# Helper function to traverse the left boundary
def traverse_left_boundary(node):
    if node:
        if node.left:
            print(node.data, end=" ")  # Print node value
            traverse_left_boundary(node.left)
        elif node.right:
            print(node.data, end=" ")  # Print node value
            traverse_left_boundary(node.right)

# Helper function to traverse the leaf nodes
def traverse_leaves(node):
    if node:
        traverse_leaves(node.left)
        if not node.left and not node.right:
            print(node.data, end=" ")  # Print leaf node value
        traverse_leaves(node.right)

# Helper function to traverse the right boundary
def traverse_right_boundary(node):
    if node:
        if node.right:
            traverse_right_boundary(node.right)
            print(node.data, end=" ")  # Print node value
        elif node.left:
            traverse_right_boundary(node.left)
            print(node.data, end=" ")  # Print node value

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
root.right.left = Node(5)
root.right.right = Node(6)

boundary_traversal(root)
