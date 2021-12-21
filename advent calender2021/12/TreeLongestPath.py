class TreeLongestPath:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 



def inorderTraversal(root):   # KESKEN,  EI  TOIMI !!!!!!!!!!!!!!

    inorderTraversalUtil(root, [])
    return 


def inorderTraversalUtil(root, path):
    if root is None:
        all_paths.append(path)
        return

    inorderTraversalUtil(root.left, path)
    path.append(root.val)
    inorderTraversalUtil(root.right, path)
    return

all_paths = []
root = TreeLongestPath(1)
root.left = TreeLongestPath(2)
root.right = TreeLongestPath(3)
root.left.left = TreeLongestPath(4)
root.left.right = TreeLongestPath(5)

inorderTraversal(root)
print(all_paths)