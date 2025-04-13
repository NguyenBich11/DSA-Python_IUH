class StudentNode:
    def __init__(self, student_id):
        self.student_id = student_id
        self.next = None

class Course:
    def __init__(self, code, title, credits, instructor, max_capacity):
        self.code = code
        self.title = title
        self.credits = credits
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.current_enrollment = 0
        self.students = None  # Head of student ID list
        self.next = None

class CourseList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def get_total_courses(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def add_to_beginning(self, code, title, credits, instructor, max_capacity):
        new_course = Course(code, title, credits, instructor, max_capacity)
        new_course.next = self.head
        self.head = new_course
        
    def add_to_end(self, code, title, credits, instructor, max_capacity):
        new_course = Course(code, title, credits, instructor, max_capacity)
        if not self.head:
            self.head = new_course
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_course
        
    def find_by_code(self, code):
        current = self.head
        while current:
            if current.code == code:
                return current
            current = current.next
        return None
    
    def display_all(self):
        if not self.head:
            print("No courses in the system.")
            return
        current = self.head
        while current:
            print(f"Code: {current.code}, Title: {current.title}, Credits: {current.credits}")
            print(f"Instructor: {current.instructor}, Capacity: {current.max_capacity}")
            print(f"Current Enrollment: {current.current_enrollment}")
            print("---")
            current = current.next
            
    def register_student(self, course_code, student_id):
        course = self.find_by_code(course_code)
        if not course or course.current_enrollment >= course.max_capacity:
            return False
        
        # Check if student is already registered
        current = course.students
        while current:
            if current.student_id == student_id:
                return False
            current = current.next
            
        new_student = StudentNode(student_id)
        new_student.next = course.students
        course.students = new_student
        course.current_enrollment += 1
        return True
    
    def drop_student(self, course_code, student_id):
        course = self.find_by_code(course_code)
        if not course or not course.students:
            return False
            
        if course.students.student_id == student_id:
            course.students = course.students.next
            course.current_enrollment -= 1
            return True
            
        current = course.students
        while current.next:
            if current.next.student_id == student_id:
                current.next = current.next.next
                course.current_enrollment -= 1
                return True
            current = current.next
        return False
    
    def list_enrolled_students(self, course_code):
        course = self.find_by_code(course_code)
        if not course:
            return []
        
        students = []
        current = course.students
        while current:
            students.append(current.student_id)
            current = current.next
        return students
    
    def get_enrollment_statistics(self):
        if not self.head:
            return None, None
        
        highest = lowest = self.head
        current = self.head
        while current:
            if current.current_enrollment > highest.current_enrollment:
                highest = current
            if current.current_enrollment < lowest.current_enrollment:
                lowest = current
            current = current.next
        return highest, lowest
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            current = self.head
            while current:
                # Save course information
                f.write(f"{current.code},{current.title},{current.credits},{current.instructor},{current.max_capacity}\n")
                # Save enrolled students
                student = current.students
                while student:
                    f.write(f"STUDENT,{current.code},{student.student_id}\n")
                    student = student.next
                current = current.next
                
    def load_from_file(self, filename):
        self.head = None
        try:
            with open(filename, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 5:  # Course information
                        code, title, credits, instructor, max_capacity = data
                        self.add_to_end(code, title, int(credits), instructor, int(max_capacity))
                    elif len(data) == 3 and data[0] == "STUDENT":  # Student enrollment
                        _, course_code, student_id = data
                        self.register_student(course_code, student_id)
            return True
        except:
            return False