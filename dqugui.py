import tkinter as tk
from tkinter import simpledialog

class DqueueGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Deque Operations")

        self.dq = Dqueue()

        self.label = tk.Label(master, text="Deque Operations", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_front_button = tk.Button(master, text="Add to Front", command=self.add_to_front, bg="lightblue", font=("Helvetica", 12))
        self.add_front_button.grid(row=1, column=0, padx=5, pady=5)

        self.add_rear_button = tk.Button(master, text="Add to Rear", command=self.add_to_rear, bg="lightgreen", font=("Helvetica", 12))
        self.add_rear_button.grid(row=1, column=1, padx=5, pady=5)

        self.delete_front_button = tk.Button(master, text="Delete from Front", command=self.delete_from_front, bg="lightcoral", font=("Helvetica", 12))
        self.delete_front_button.grid(row=2, column=0, padx=5, pady=5)

        self.delete_rear_button = tk.Button(master, text="Delete from Rear", command=self.delete_from_rear, bg="lightyellow", font=("Helvetica", 12))
        self.delete_rear_button.grid(row=2, column=1, padx=5, pady=5)

        self.search_button = tk.Button(master, text="Search Element", command=self.search_element, bg="lightgrey", font=("Helvetica", 12))
        self.search_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.display_button = tk.Button(master, text="Display Deque", command=self.display_deque, bg="lightpink", font=("Helvetica", 12))
        self.display_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit, bg="lightgrey", font=("Helvetica", 12))
        self.exit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.deque_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.deque_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_to_front(self):
        element = simpledialog.askstring("Add to Front", "Enter element to add to front:")
        if element:
            self.dq.add_front(element)
            self.display_deque()

    def add_to_rear(self):
        element = simpledialog.askstring("Add to Rear", "Enter element to add to rear:")
        if element:
            self.dq.add_rear(element)
            self.display_deque()

    def delete_from_front(self):
        deleted_value = self.dq.delete_front()
        if deleted_value != -1:
            self.display_deque()
        else:
            self.update_deque_label("Deque Underflow")

    def delete_from_rear(self):
        deleted_value = self.dq.delete_rear()
        if deleted_value != -1:
            self.display_deque()
        else:
            self.update_deque_label("Deque Underflow")

    def search_element(self):
        element = simpledialog.askstring("Search Element", "Enter element to search:")
        if element:
            result = self.dq.search(element)
            if result != -1:
                self.update_deque_label(f"Element found at position: {result}")
            elif result == -2:
                self.update_deque_label("Element not found in the Deque")
            else:
                self.update_deque_label("Deque is empty")

    def display_deque(self):
        deque_content = self.dq.display()
        self.update_deque_label(f"Deque: {deque_content}")

    def update_deque_label(self, message):
        self.deque_label.config(text=message)


class Dqueue:
    def __init__(self):
        self.dq = []

    def isempty(self):
        return self.dq == []

    def add_front(self, element):
        self.dq.insert(0, element)

    def add_rear(self, element):
        self.dq.append(element)

    def delete_front(self):
        if self.isempty():
            return -1
        else:
            return self.dq.pop(0)

    def delete_rear(self):
        if self.isempty():
            return -1
        else:
            return self.dq.pop()

    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.dq.index(element)
                return n + 1
            except ValueError:
                return -2

    def display(self):
        return self.dq


def main():
    root = tk.Tk()
    app = DqueueGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()