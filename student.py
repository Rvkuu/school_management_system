# student.py
class StudentMemento:
    """Memento object that stores the state of a student."""
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade


class Student:
    """Represents a single student record."""

    def __init__(self, student_id: int, name: str, age: int, grade: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    # --- Memento support ---
    def save_state(self):
        """Save current state into a memento object."""
        return StudentMemento(self.student_id, self.name, self.age, self.grade)

    def restore_state(self, memento: StudentMemento):
        """Restore student state from a memento object."""
        self.name = memento.name
        self.age = memento.age
        self.grade = memento.grade
