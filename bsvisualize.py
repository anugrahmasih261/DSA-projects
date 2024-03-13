import turtle

def binary(arr, target, visualization=False):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if visualization:
            draw_search_state(arr, left, right, mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def draw_search_state(arr, left, right, mid):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # Draw the array
    for i, num in enumerate(arr):
        if i == mid:
            turtle.color("red")
        elif left <= i <= right:
            turtle.color("black")
        else:
            turtle.color("gray")
        turtle.write(str(num), align="center", font=("Arial", 12, "normal"))
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()

    # Draw pointers
    turtle.penup()
    turtle.goto(left * 40 - 20, -50)
    turtle.pendown()
    turtle.write("left", align="center", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(right * 40 + 20, -50)
    turtle.pendown()
    turtle.write("right", align="center", font=("Arial", 12, "normal"))
    turtle.penup()
    turtle.goto(mid * 40, -80)
    turtle.pendown()
    turtle.write("mid", align="center", font=("Arial", 12, "normal"))

    turtle.hideturtle()
    turtle.update()

def main():
    turtle.setup(800, 200)
    turtle.speed(0)
    arr = [1, 2, 3, 4, 5, 6, 7,88,99,101,102,103,   104, 105, 106,  107, 108, 109, 110]
    target = int(input('Enter the number to search for: '))
    re = binary(arr, target, visualization=True)
    if re == -1:
        print(target, 'not found')
    else:
        print(target, 'found at', re)

    turtle.done()

if __name__ == "__main__":
    main()
