class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def sum_tree_values(node):
    if node is None:
        return 0  # Якщо вузол порожній, повертаємо 0
    left_sum = sum_tree_values(node.left)
    right_sum = sum_tree_values(node.right)
    return node.value + left_sum + right_sum


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(30)

    print(sum_tree_values(root))


if __name__ == "__main__":
    main()