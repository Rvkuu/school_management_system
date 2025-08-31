# school_management_system
A group project by Yusra Adeyeri and Ubi Precious

# Summary
We decided to design a simple school management system that will simulate the creation and management of student data.
The project is to explain how a system's architecture looks with and without design patterns.
In the first commit, the school management system will have Object Oriented Principles like encapsulation, abstraction, polymorphism etc.
In the second commit, the school management system will have design patterns like memento.

# First Commit
The first commit has the student.py class, school.py class and the main.py file. The code snippet that was committed shows some Object Oriented Programming attributes like:
-   Encapsulation: This is seen in the student.py class where each student is an object (Student) with attributes and methods. The student.py handles student data.
-   Abstraction: This is seen in the school.py class where school manages the list of students and details are hidden inside methods.
-   Polymorphism: The __str__ method makes printing student objects easy.
-   Reusability: The system is modular and extendable.

# student.py
The student.py is a class called student. Here each object of student will represent a real student attributes like ID, Name, Age and Grade.
The constructor method __init__ is called automatically when a new student object is created and the self keyword refers to the current object.
An instance method for updating student information where parameters default to None; meaning you don't have to provide all of them when updating. The if checks make sure we only update values that are given.
The __str__ method defines how the student object looks when you print()

# school.py
In the school.py class, we import the Student class from student.py, this will allow us create and manange Student objects inside the School class.
The School class acts as the database of the system and manages a list of Student objects.
The constructor method for the School class will have an empty list that will store all Student objects (self.student = []) and a counter used to assign unique IDs to new students and each time a student is added,the ID increases by 1 (self.next_id = 1).
The add_student is a method to add a new student by creating new Student object with the current next_id and appends this student to the students list. The next student gets a new unique ID by implementing increments on next_id (self.next_id += 1).
The find_student is a helper method for student search by ID. It loops through the students list and returns that student objects that matches the given student_id to all the student's id. However, if no match is found, return None.
The update_student updates student details by first calling find_student to locate the student by ID. If the student is found, it calls the student's own .update() method from (student.py) and if not found - else: print("Student not found) as an error message.
delete_student calls find_student just like the update_student. If the student is found, it removes it from the students list and if not found, an error message is printed.
list_students displays all students in the system. If the list is empty "No students" is printed. The print(student) calls student.__str__() automaticall from (student.py).
In summary, School acts like the manager of student records and stores all Student objects in a list. It also handles Add, Update, Delete, List operations and uses find_student() as a helper to locate students by ID.

# main.py
The main.py imports school from School and this allows us to create a School object and use its methods (add_student, update_student, etc).
main() will run the system and inside it we create an object school = School(). This means we now have a "school manager" ready to hold and manipulate student records.
The menu loop runs forever (while True) until the user chooses Exit. It displays options to the user (Add, Update, Delete, List, Exit) and takes input from the user (choice) as a string.
-   Option 1: Add Student - This collects name, age, and grade from the user. It calls school.add_student(), which creates a new Student and adds it to the list.
-   Option 2: Update Student - This asks for the student's ID, also asks for new values (name, age, grade) but user can leave them blank. The age_input is converted to an integer only if provided. It calls school.update_student(...), which finds the student and updates only the given fields.
-   Option 3: Delete Student - This asks for a student ID. It calls school.delete_student(...), which finds and removes that student from the list.
-   Option 4: List Students - This calls school.list_students() and prints all students in the system or says none exist.
-   Option 5: Exit - This breaks out of the while True loop and the program ends with a goodbye message.
The user inputs anything outside 1-5, the program warns them and loops back.

#       Memento
Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

# Second Commit: Momento
In a school management system that handles student records, Memento (a design pattern that supports undo/restore of student records) is useful. However, the memento design method requires the ability to store history(snapshots) and this is possible using a Caretaker class
Each student has a state (id, name, age, grade) and we may sometimes want to save a snapshot of a student record and restore it later, for instance, undo the last update on the school management system, the Memento design pattern captures and restores an object's state without exposing is internal process.
This is implemented in the extension of the student class to support saving/restoring snapshots, a memento class will be created that holds students state and also, the caretaker class to manage history (like an undo stack).
The code snippets in the second commit uses some design patterns like:
-   Memento
-   Facade
-   Singleton

# caretaker.py
In the memento design pattern, the caretaker is responsible for managing saved states (Mementos) of an object, without modifyiing them directly. It doesn't know what is inside the Memento (encapsulation is preserved), it only stores them in undo/redo stacks and applies them when asked and lastly, it makes the system behave like an editor (undo/redo functionality)
The caretaker class has the __init__ constructor that initializes the undo_stack function and redo_stack function. The self.undo_stack = [] is a list that holds past ststes (so we can go backwards = undo) while the self.redo_stack = [] is a list that holds undone states (so we can go forwards = redo).
When we call save(student) before modifying a student, student.save() creates a memento object containing the student's current state (ID, name, age, grade) that is stored in the undo.stack.
The redo_stack is cleared because whenever you perform a new action, the "redo history" becomes invalid (just like MS Word or Photoshop).
If undo_stack is empty, there will be nothing to undo. Otherwise:
-   memento = self.undo_stack.pop() -> take the most recent saved state.
-   self.redo_stack.append(memento) -> pushes it to redo_stack so we can redo later.
-   memento.restore() -> reverts the Student object back to the state stored in the memento.
if redo_stack is empty, there will be nothing to redo. Otherwise:
-   memento = self.redo_stack.pop() -> gets the most recent undone state.
-   self.undo_stack.append(memento) -> moves it back to undo history.
-   memento.restore() -> reapplies the undone change.

# school.py
The school.py class in the second commit is an update file with the addition on the imports (from caretaker import Caretaker). Also, the school.py implements the singleton design pattern when being initialized. _instance = None is used for the Singleton design pattern, ensuring only one School object exists throughout the program. The constructor def __new__(cls): is a special methos in Python that controls object creation before the __int__.
-   if cls._instance is None: -> If no instance exists yet, create one.
Inside the block, initialize:
-   students = [] list to store all students objects.
-   caretaker = Caretaker() attaches a caretaker instance for undo/redo.
-   next_id = 1 increases the ID counter for students automatically.
-   return cls._instance always returns the same instance, making School a Singleton.

# student.py
The __init__ constructor initializes a new student object with:
-   student_id given by School
-   name
-   age
-   grade
And each of this value is assigned to self, so it belongs to the object.
The Memento design can be seen implemented in the save_state method, when initialized, it creates a snapshot of the current state of the student and returns a Student.Memento object holding the student's current data. The snapshot can later be used to restore this exact state.
Also in the restore_state method, it restores the student's data from a Memento, which essentially rolls back or re-applies a change depending on undp/redo.
The memento inner class is used to store snapshots of a student and each memento object holds a frozen copy of student data. The memento has the same field as Student (id, name, age, grade) but does not change.

# main.py
The main.py file still defines the entry point function where the system will start running.
Notice that the choices for options 5 and 6 are now different from the first commit.
With the addition of the Memento Design Pattern to the code architecture, we notice the addition of the "Undo last action" and the "Redo last action"