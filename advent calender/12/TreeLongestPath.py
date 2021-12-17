class TreeLongestPath:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def inorderTraversal(root):   # KESKEN,  EI  TOIMI !!!!!!!!!!!!!!
    longest = []

    inorderTraversalUtil(root, longest)
    return longest


def inorderTraversalUtil(root, longest):
    if root is None:
        return

    inorderTraversalUtil(root.left, longest)
    longest.append(root.val)
    inorderTraversalUtil(root.right, longest)
    return


root = TreeLongestPath(1)
root.left = TreeLongestPath(2)
root.right = TreeLongestPath(3)
root.left.left = TreeLongestPath(4)
root.left.right = TreeLongestPath(5)

print(inorderTraversal(root))