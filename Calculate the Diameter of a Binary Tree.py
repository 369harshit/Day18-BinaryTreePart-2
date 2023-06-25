class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    if not root:
        return 0

    def depth(node):
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)
        
        # Calculate the path length passing through the current node
        node_diameter = left_depth + right_depth
        
        # Update the global maximum diameter if necessary
        diameterOfBinaryTree.max_diameter = max(diameterOfBinaryTree.max_diameter, node_diameter)
        
        # Return the maximum depth from the current node
        return max(left_depth, right_depth) + 1

    # Initialize the global maximum diameter variable
    diameterOfBinaryTree.max_diameter = 0

    # Start the depth-first search from the root node
    depth(root)

    # Return the maximum diameter found
    return diameterOfBinaryTree.max_diameter

# Example binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calculate the diameter of the binary tree
diameter = diameterOfBinaryTree(root)
print("Diameter of the binary tree:", diameter)
