class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
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

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def count_leaves(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

if __name__ == "__main__":
    tree = BinarySearchTree()
    
    # Test insert and traversal
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        tree.insert(value)

    print("Inorder traversal:")
    tree.inorder(tree.root)
    print("\nNumber of leaves:", tree.count_leaves(tree.root))
    print("Height of tree:", tree.height(tree.root))
    
    # Test search
    search_value = 4
    result = tree.search(search_value)
    print(f"\nSearching for {search_value}: {'Found' if result else 'Not found'}")
    
    # Test delete
    delete_value = 3
    print(f"\nDeleting {delete_value}")
    tree.delete(delete_value)
    print("Inorder traversal after deletion:")
    tree.inorder(tree.root)