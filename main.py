# main.py
from school import School

def main():
    school = School()

    while True:
        print("\n=== School Management System (OOP with Singleton + Memento) ===")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Undo Last Action")
        print("6. Redo Last Action")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            school.add_student(name, age, grade)

        elif choice == "2":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (or leave blank): ")
            age_input = input("Enter new age (or leave blank): ")
            grade = input("Enter new grade (or leave blank): ")

            age = int(age_input) if age_input else None
            school.update_student(student_id, name if name else None, age, grade if grade else None)

        elif choice == "3":
            student_id = int(input("Enter student ID to delete: "))
            school.delete_student(student_id)

        elif choice == "4":
            school.list_students()

        elif choice == "5":
            school.undo_last_action()

        elif choice == "6":
            school.redo_last_action()

        elif choice == "7":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
