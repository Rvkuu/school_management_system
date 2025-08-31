# school.py
from student import Student
from caretaker import Caretaker


class School:
    """Singleton class that manages students using Memento for undo/redo."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(School, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "students"):  # Avoid reinitialization
            self.students = {}
            self.next_id = 1
            self.caretaker = Caretaker()

    # ---------------- CRUD Operations ----------------

    def add_student(self, name, age, grade):
        student = Student(self.next_id, name, age, grade)
        self.students[self.next_id] = student
        self.caretaker.save_state(("add", student.save_state()))
        print(f"Student added: {student}")
        self.next_id += 1

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]
        # Save old state before updating
        self.caretaker.save_state(("update", student.save_state()))

        if name:
            student.name = name
        if age is not None:
            student.age = age
        if grade:
            student.grade = grade

        print(f"Student updated: {student}")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students.pop(student_id)
        self.caretaker.save_state(("delete", student.save_state()))
        print(f"Student deleted: {student}")

    def list_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

    # ---------------- Undo/Redo ----------------

    def undo_last_action(self):
        memento_info = self.caretaker.undo()
        if not memento_info:
            print("Nothing to undo.")
            return

        action, memento = memento_info

        if action == "add":
            # Undo add → remove the student
            if memento.student_id in self.students:
                removed = self.students.pop(memento.student_id)
                print(f"Undo Add: Removed {removed}")

        elif action == "update":
            # Undo update → restore old state
            if memento.student_id in self.students:
                self.students[memento.student_id].restore_state(memento)
                print(f"Undo Update: Restored {self.students[memento.student_id]}")

        elif action == "delete":
            # Undo delete → re-add the student
            restored = Student(memento.student_id, memento.name, memento.age, memento.grade)
            self.students[memento.student_id] = restored
            print(f"Undo Delete: Restored {restored}")

    def redo_last_action(self):
        memento_info = self.caretaker.redo()
        if not memento_info:
            print("Nothing to redo.")
            return

        action, memento = memento_info

        if action == "add":
            # Redo add → re-add the student
            restored = Student(memento.student_id, memento.name, memento.age, memento.grade)
            self.students[memento.student_id] = restored
            print(f"Redo Add: Restored {restored}")

        elif action == "update":
            # Redo update → reapply update (simply restoring state again)
            if memento.student_id in self.students:
                self.students[memento.student_id].restore_state(memento)
                print(f"Redo Update: {self.students[memento.student_id]}")

        elif action == "delete":
            # Redo delete → remove again
            if memento.student_id in self.students:
                removed = self.students.pop(memento.student_id)
                print(f"Redo Delete: Removed {removed}")
