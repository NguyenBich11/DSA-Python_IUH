class Student:
    def __init__(self, student_id, name, major, gpa):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def get_total_students(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def add_to_beginning(self, student_id, name, major, gpa):
        new_student = Student(student_id, name, major, gpa)
        new_student.next = self.head
        self.head = new_student
        
    def add_to_end(self, student_id, name, major, gpa):
        new_student = Student(student_id, name, major, gpa)
        if not self.head:
            self.head = new_student
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_student
        
    def add_after_id(self, target_id, student_id, name, major, gpa):
        current = self.head
        while current:
            if current.student_id == target_id:
                new_student = Student(student_id, name, major, gpa)
                new_student.next = current.next
                current.next = new_student
                return True
            current = current.next
        return False
    
    def display_all(self):
        if not self.head:
            print("No students in the system.")
            return
        current = self.head
        while current:
            print(f"ID: {current.student_id}, Name: {current.name}, Major: {current.major}, GPA: {current.gpa}")
            current = current.next
            
    def find_by_id(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                return current
            current = current.next
        return None
    
    def update_student(self, student_id, name, major, gpa):
        student = self.find_by_id(student_id)
        if student:
            student.name = name
            student.major = major
            student.gpa = gpa
            return True
        return False
    
    def remove_from_beginning(self):
        if not self.head:
            return False
        self.head = self.head.next
        return True
    
    def remove_from_end(self):
        if not self.head:
            return False
        if not self.head.next:
            self.head = None
            return True
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        return True
    
    def remove_by_id(self, student_id):
        if not self.head:
            return False
        if self.head.student_id == student_id:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.student_id == student_id:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def sort_by_gpa(self, ascending=True):
        if not self.head:
            return
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append((current.student_id, current.name, current.major, current.gpa))
            current = current.next
        sorted_list.sort(key=lambda x: x[3], reverse=not ascending)
        self.head = None
        for student in sorted_list:
            self.add_to_end(*student)
            
    def find_extreme_gpas(self):
        if not self.head:
            return None, None
        highest = lowest = self.head
        current = self.head
        while current:
            if current.gpa > highest.gpa:
                highest = current
            if current.gpa < lowest.gpa:
                lowest = current
            current = current.next
        return highest, lowest
    
    def major_report(self):
        major_count = {}
        current = self.head
        while current:
            major_count[current.major] = major_count.get(current.major, 0) + 1
            current = current.next
        return major_count
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            current = self.head
            while current:
                f.write(f"{current.student_id},{current.name},{current.major},{current.gpa}\n")
                current = current.next
                
    def load_from_file(self, filename):
        self.head = None
        try:
            with open(filename, 'r') as f:
                for line in f:
                    student_id, name, major, gpa = line.strip().split(',')
                    self.add_to_end(student_id, name, major, float(gpa))
            return True
        except:
            return False