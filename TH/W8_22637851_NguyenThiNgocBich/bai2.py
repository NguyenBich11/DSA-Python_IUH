class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def sum_tree(self, node):
        if not node:
            return 0
        return node.value + self.sum_tree(node.left) + self.sum_tree(node.right)

    def find_max(self, node):
        if not node:
            return float('-inf')
        current = node
        while current.right:
            current = current.right
        return current.value

    def find_min(self, node):
        if not node:
            return float('inf')
        current = node
        while current.left:
            current = current.left
        return current.value

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def count_leaves(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        tree.insert(value)

    print("Sum of all nodes:", tree.sum_tree(tree.root))
    print("Maximum value:", tree.find_max(tree.root))
    print("Minimum value:", tree.find_min(tree.root))
    print("Total number of nodes:", tree.count_nodes(tree.root))
    print("Number of leaf nodes:", tree.count_leaves(tree.root))