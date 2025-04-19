class Student:
    def __init__(self, masv, hoten, malop, diemtb):
        self.masv = masv
        self.hoten = hoten
        self.malop = malop
        self.diemtb = diemtb

    def __str__(self):
        return f"MASV: {self.masv}, Ho ten: {self.hoten}, Ma lop: {self.malop}, Diem TB: {self.diemtb}"

class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if not self.root:
            self.root = Node(student)
        else:
            self._insert_recursive(self.root, student)

    def _insert_recursive(self, node, student):
        if student.masv < node.student.masv:
            if node.left is None:
                node.left = Node(student)
            else:
                self._insert_recursive(node.left, student)
        elif student.masv > node.student.masv:
            if node.right is None:
                node.right = Node(student)
            else:
                self._insert_recursive(node.right, student)
        else:
            return False  # MASV already exists
        return True

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.student)
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

    def search(self, masv):
        return self._search_recursive(self.root, masv)

    def _search_recursive(self, node, masv):
        if not node or node.student.masv == masv:
            return node
        if masv < node.student.masv:
            return self._search_recursive(node.left, masv)
        return self._search_recursive(node.right, masv)

    def delete(self, masv):
        self.root = self._delete_recursive(self.root, masv)

    def _delete_recursive(self, node, masv):
        if not node:
            return None
        if masv < node.student.masv:
            node.left = self._delete_recursive(node.left, masv)
        elif masv > node.student.masv:
            node.right = self._delete_recursive(node.right, masv)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_node = self._find_min(node.right)
            node.student = min_node.student
            node.right = self._delete_recursive(node.right, min_node.student.masv)
        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

if __name__ == "__main__":
    tree = StudentBST()
    
    # Test data
    students = [
        Student("SV001", "Nguyen Van A", "CNTT1", 8.5),
        Student("SV003", "Tran Thi B", "CNTT2", 7.5),
        Student("SV002", "Le Van C", "CNTT1", 9.0)
    ]
    
    # Insert students
    for student in students:
        if tree.insert(student):
            print(f"Added student: {student.masv}")
        else:
            print(f"Student {student.masv} already exists")

    print("\nInorder traversal (sorted by MASV):")
    tree.inorder(tree.root)
    
    print(f"\nNumber of leaves: {tree.count_leaves(tree.root)}")
    print(f"Height of tree: {tree.height(tree.root)}")
    
    # Test search
    search_masv = "SV001"
    result = tree.search(search_masv)
    if result:
        print(f"\nFound student: {result.student}")
    else:
        print(f"\nStudent {search_masv} not found")
    
    # Test delete
    delete_masv = "SV002"
    print(f"\nDeleting student {delete_masv}")
    tree.delete(delete_masv)
    print("\nAfter deletion:")
    tree.inorder(tree.root)