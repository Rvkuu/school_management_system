# school.py
from student import Student


class School:
    """Manages all students"""

    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self, name, age, grade):
        student = Student(self.next_id, name, age, grade)
        self.students.append(student)
        self.next_id += 1
        print(f"Student {name} added successfully!")

    def find_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def update_student(self, student_id, name=None, age=None, grade=None):
        student = self.find_student(student_id)
        if student:
            student.update(name, age, grade)
            print(f"Student {student_id} updated successfully!")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Student {student_id} deleted successfully!")
        else:
            print("Student not found.")

    def list_students(self):
        if not self.students:
            print("No students in the system.")
            return
        print("\n--- Student Records ---")
        for student in self.students:
            print(student)
        print("-------------------------")

    def add_student_subject(self, student_id, subject, mark):
        """Assign a subject and mark to a student"""
        student = self.find_student(student_id)
        if student:
            student.add_subject(subject, mark)
        else:
            print("Student not found.")
