import tkinter as tk
from tkinter import simpledialog

class QueueGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Queue Operations")

        self.q = Queue()
        
        self.label = tk.Label(master, text="Queue Operations", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(master, text="Add Element", command=self.add_element, bg="lightblue", font=("Helvetica", 12))
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Element", command=self.delete_element, bg="lightgreen", font=("Helvetica", 12))
        self.delete_button.grid(row=1, column=1, padx=5, pady=5)

        self.search_button = tk.Button(master, text="Search Element", command=self.search_element, bg="lightyellow", font=("Helvetica", 12))
        self.search_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(master, text="Queue: " + self.q.display(), font=("Helvetica", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit, bg="lightgrey", font=("Helvetica", 12))
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_element(self):
        element = simpledialog.askstring("Add Element", "Enter element to add:")
        if element:
            self.q.add(element)
            self.update_result_label()

    def delete_element(self):
        deleted_value = self.q.delete()
        if deleted_value != -1:
            self.update_result_label("Deleted element: " + deleted_value)
        else:
            self.update_result_label("Queue Underflow")

    def search_element(self):
        element = simpledialog.askstring("Search Element", "Enter element to search:")
        if element:
            result = self.q.search(element)
            if result != -1:
                self.update_result_label("Element '{}' found at position {}.".format(element, result))
            else:
                self.update_result_label("Element '{}' not found.".format(element))

    def update_result_label(self, message=None):
        result_text = "Queue: " + self.q.display()
        if message:
            result_text += "\n" + message
        self.result_label.config(text=result_text)

class Queue:
    def __init__(self):
        self.qu = []

    def isempty(self):
        return self.qu == []

    def add(self, element):
        self.qu.append(element)

    def delete(self):
        if self.isempty():
            return -1
        else:
            return self.qu.pop(0)

    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.qu.index(element)
                return n + 1
            except ValueError:
                return -1

    def display(self):
        return ", ".join(self.qu)

def main():
    root = tk.Tk()
    app = QueueGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
