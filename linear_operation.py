import turtle
import tkinter as tk

def linear_search(arr, target, visualization_canvas=None):
    for i in range(len(arr)):
        if arr[i] == target:
            if visualization_canvas:
                draw_search_state(arr, i, visualization_canvas)
            return i
    return -1

def draw_search_state(arr, index, canvas):
    canvas.delete("all")

    # Draw the array
    for i, num in enumerate(arr):
        if i == index:
            color = "red"
        else:
            color = "black"
        canvas.create_text(i * 40 + 20, 20, text=str(num), fill=color, font=("Arial", 12, "normal"))

    # Draw pointer
    canvas.create_text(index * 40 + 20, 50, text="current", fill="blue", font=("Arial", 12, "normal"))

def search_button_clicked():
    target = int(entry.get())
    re = linear_search(arr, target, visualization_canvas)
    if re == -1:
        result_label.config(text=f"{target} not found")
    else:
        result_label.config(text=f"{target} found at index {re}")

# Initialize Tkinter window
window = tk.Tk()
window.title("Linear Search Visualization")
window.geometry("800x200")

# Create Tkinter canvas for visualization
visualization_canvas = tk.Canvas(window, width=800, height=100)
visualization_canvas.pack()

# Create entry widget for user input
entry_label = tk.Label(window, text="Enter the number to search for:")
entry_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create search button
search_button = tk.Button(window, text="Search", command=search_button_clicked)
search_button.pack()

# Create label to display search result
result_label = tk.Label(window, text="")
result_label.pack()

# Define array to search
arr = [1, 2, 3, 4, 5, 6, 7, 88, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

# Start Tkinter event loop
window.mainloop()
