# student.py

class Student:
    """Represents a single student"""

    def __init__(self, student_id, name, age, grade):
        self.id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = {}  # Dictionary: {subject: mark}

    def update(self, name=None, age=None, grade=None):
        """Update student details"""
        if name:
            self.name = name
        if age:
            self.age = age
        if grade:
            self.grade = grade

    def add_subject(self, subject, mark):
        """Add or update a subject mark"""
        self.subjects[subject] = mark
        print(f"Added/Updated {subject} for {self.name} with mark {mark}")

    def calculate_average(self):
        """Calculate average mark across subjects"""
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def __str__(self):
        """String representation of student"""
        subjects_info = (
            ", ".join([f"{sub}:{mark}" for sub, mark in self.subjects.items()])
            if self.subjects else "No subjects"
        )
        avg = self.calculate_average()
        return f"ID: {self.id} | Name: {self.name} | Age: {self.age} | Grade: {self.grade} | Subjects: {subjects_info} | Avg: {avg:.2f}"
