import turtle
import time

def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    index = partition(arr, left, right, pivot)
    quick_sort(arr, left, index - 1)
    quick_sort(arr, index, right)

def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            draw_sort_state(arr, left, right)
    return left

def draw_sort_state(arr, left, right):
    turtle.clear()
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()

    for i, num in enumerate(arr):
        if left <= i <= right:
            turtle.color("red")
        else:
            turtle.color("black")
        turtle.write(str(num), align="center", font=("Arial", 12, "normal"))
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()

    turtle.hideturtle()
    turtle.update()
    time.sleep(1)  # Delay for visualization

def main():
    turtle.setup(800, 200)
    turtle.speed(0)
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original Array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array:", arr)

    turtle.done()

if __name__ == "__main__":
    main()
