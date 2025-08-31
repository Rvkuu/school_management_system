# caretaker.py
class Caretaker:
    """Caretaker manages undo/redo stacks of mementos."""

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self, memento):
        """Save a new state and clear redo history."""
        self.undo_stack.append(memento)
        self.redo_stack.clear()

    def undo(self):
        """Undo last state change (moves it to redo stack)."""
        if not self.undo_stack:
            return None
        memento = self.undo_stack.pop()
        self.redo_stack.append(memento)
        return memento

    def redo(self):
        """Redo the last undone state."""
        if not self.redo_stack:
            return None
        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento
