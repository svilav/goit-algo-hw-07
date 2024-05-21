class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_min_value(node):
    if node is None:
        return None  # Дерево порожнє
    current = node
    while current.left is not None:
        current = current.left
    return current.value


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    print(find_min_value(root))


if __name__ == "__main__":
    main()