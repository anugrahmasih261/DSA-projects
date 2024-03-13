import tkinter as tk
from tkinter import simpledialog

class StackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stack Operations")

        self.s = Stack()
        
        self.label = tk.Label(master, text="Stack Operations", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.push_button = tk.Button(master, text="Push Element", command=self.push_element, bg="lightblue", font=("Helvetica", 12))
        self.push_button.grid(row=1, column=0, padx=5, pady=5)

        self.pop_button = tk.Button(master, text="Pop Element", command=self.pop_element, bg="lightgreen", font=("Helvetica", 12))
        self.pop_button.grid(row=1, column=1, padx=5, pady=5)

        self.peep_button = tk.Button(master, text="Peep Element", command=self.peep_element, bg="lightcoral", font=("Helvetica", 12))
        self.peep_button.grid(row=2, column=0, padx=5, pady=5)

        self.search_button = tk.Button(master, text="Search Element", command=self.search_element, bg="lightyellow", font=("Helvetica", 12))
        self.search_button.grid(row=2, column=1, padx=5, pady=5)

        self.result_label = tk.Label(master, text="Stack: " + self.s.display(), font=("Helvetica", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit, bg="lightgrey", font=("Helvetica", 12))
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def push_element(self):
        element = simpledialog.askstring("Push Element", "Enter element to push:")
        if element:
            self.s.push(element)
            self.update_result_label()

    def pop_element(self):
        try:    
            popped_value = self.s.pop()
            self.update_result_label("Popped element: " + popped_value)
        except IndexError:
            self.update_result_label("Stack Underflow")

    def peep_element(self):
        try:
            top_value = self.s.peep()
            self.update_result_label("Top element: " + top_value)
        except IndexError:
            self.update_result_label("Stack Empty")

    def search_element(self):
        element = simpledialog.askstring("Search Element", "Enter element to search:")
        if element:
            result = self.s.search(element)
            if result != -1:
                self.update_result_label("Element '{}' found at position {}.".format(element, result + 1))
            else:
                self.update_result_label("Element '{}' not found.".format(element))

    def update_result_label(self, message=None):
        result_text = "Stack: " + self.s.display()
        if message:
            result_text += "\n" + message
        self.result_label.config(text=result_text)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack Underflow")

    def peep(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack Empty")

    def search(self, element):
        try:
            return self.stack.index(element)
        except ValueError:
            return -1

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return ", ".join(self.stack)

def main():
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
