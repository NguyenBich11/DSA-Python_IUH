class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # 1. Kiểm tra cây rỗng
    def is_empty(self):
        return self.root is None

    # 2. Kiểm tra nút n có phải là nút lá không
    def is_leaf(self, node):
        if not node:
            return False
        return node.left is None and node.right is None

    # 3. Kiểm tra nút n có phải là nút cha của nút m không
    def is_parent(self, n, m):
        if not n or not m:
            return False
        return n.left == m or n.right == m

    # 4. Tính chiều cao của cây
    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    # 5. Tính số nút của cây
    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # 6. Duyệt tiền tự, trung tự, hậu tự
    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

    # 7. Đếm số nút lá của cây
    def count_leaves(self, node):
        if not node:
            return 0
        if self.is_leaf(node):
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    # 8. Đếm số nút trung gian của cây
    def count_internal_nodes(self, node):
        if not node or self.is_leaf(node):
            return 0
        return 1 + self.count_internal_nodes(node.left) + self.count_internal_nodes(node.right)

    # 9. Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút
    def find_max(self, node):
        if not node:
            return float('-inf')
        max_value = node.value
        left_max = self.find_max(node.left)
        right_max = self.find_max(node.right)
        return max(max_value, left_max, right_max)

    def find_min(self, node):
        if not node:
            return float('inf')
        min_value = node.value
        left_min = self.find_min(node.left)
        right_min = self.find_min(node.right)
        return min(min_value, left_min, right_min)

    def sum_nodes(self, node):
        if not node:
            return 0
        return node.value + self.sum_nodes(node.left) + self.sum_nodes(node.right)

    def average_nodes(self, node):
        total = self.sum_nodes(node)
        count = self.count_nodes(node)
        return total / count if count > 0 else 0

# Test the implementation
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Is tree empty?", tree.is_empty())
    print("Is node a leaf?", tree.is_leaf(tree.root.left.left))
    print("Height of tree:", tree.height(tree.root))
    print("Number of nodes:", tree.count_nodes(tree.root))
    
    print("\nPreorder traversal:")
    tree.preorder(tree.root)
    print("\nInorder traversal:")
    tree.inorder(tree.root)
    print("\nPostorder traversal:")
    tree.postorder(tree.root)
    
    print("\nNumber of leaves:", tree.count_leaves(tree.root))
    print("Number of internal nodes:", tree.count_internal_nodes(tree.root))
    print("Maximum value:", tree.find_max(tree.root))
    print("Minimum value:", tree.find_min(tree.root))
    print("Sum of nodes:", tree.sum_nodes(tree.root))
    print("Average of nodes:", tree.average_nodes(tree.root))