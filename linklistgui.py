import tkinter as tk
from tkinter import simpledialog

class LinkedListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Linked List Operations")

        self.link_list = ['America', 'Japan', 'India']

        self.label = tk.Label(master, text="Linked List Operations", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(master, text="Add Element", command=self.add_element, bg="lightblue", font=("Helvetica", 12))
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(master, text="Remove Element", command=self.remove_element, bg="lightgreen", font=("Helvetica", 12))
        self.remove_button.grid(row=1, column=1, padx=5, pady=5)

        self.replace_button = tk.Button(master, text="Replace Element", command=self.replace_element, bg="lightcoral", font=("Helvetica", 12))
        self.replace_button.grid(row=2, column=0, padx=5, pady=5)

        self.search_button = tk.Button(master, text="Search Element", command=self.search_element, bg="lightyellow", font=("Helvetica", 12))
        self.search_button.grid(row=2, column=1, padx=5, pady=5)

        self.result_label = tk.Label(master, text="Linked List: " + ", ".join(self.link_list), font=("Helvetica", 14))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit, bg="lightgrey", font=("Helvetica", 12))
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_element(self):
        element = simpledialog.askstring("Add Element", "Enter element to add:")
        if element:
            pos = simpledialog.askinteger("Add Element", "At what position you want to add:")
            if pos is not None:
                self.link_list.insert(pos, element)
                self.update_result_label()

    def remove_element(self):
        element = simpledialog.askstring("Remove Element", "Enter element to remove:")
        if element:
            try:
                self.link_list.remove(element)
                self.update_result_label()
            except ValueError:
                print("Element not found, so cannot remove.")

    def replace_element(self):
        element = simpledialog.askstring("Replace Element", "Enter new element to replace:")
        if element:
            pos = simpledialog.askinteger("Replace Element", "At what position you want to replace:")
            if pos is not None:
                if 0 <= pos < len(self.link_list):
                    replaced_element = self.link_list[pos]
                    self.link_list[pos] = element
                    self.update_result_label("Replaced '{}' at position {} with '{}'.".format(replaced_element, pos, element))
                else:
                    self.update_result_label("Invalid position. Cannot replace element.")

    def search_element(self):
        element = simpledialog.askstring("Search Element", "Enter element to search:")
        if element:
            try:
                pos = self.link_list.index(element)
                self.update_result_label("Element '{}' found at position {}.".format(element, pos))
            except ValueError:
                self.update_result_label("Element '{}' not found.".format(element))

    def update_result_label(self, message=None):
        result_text = "Linked List: " + ", ".join(self.link_list)
        if message:
            result_text += "\n" + message
        self.result_label.config(text=result_text)

def main():
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
