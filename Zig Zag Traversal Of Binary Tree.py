class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    dfs(root, 0, result)
    return result

def dfs(node, level, result):
    if not node:
        return

    if len(result) <= level:
        result.append([])

    if level % 2 == 0:
        result[level].append(node.val)
    else:
        result[level].insert(0, node.val)

    dfs(node.left, level + 1, result)
    dfs(node.right, level + 1, result)

# Example binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Perform zigzag traversal
zigzag_result = zigzagLevelOrder(root)
print("Zigzag Traversal:")
for level in zigzag_result:
    print(level,end=" ")
