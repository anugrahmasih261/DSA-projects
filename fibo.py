import turtle

def draw_circle(radius):
    turtle.circle(radius)

def fibo(n):
    fibo_seq = [0, 1]
    for i in range(2, n):
        fibo_seq.append(fibo_seq[i-1] + fibo_seq[i-2])
    return fibo_seq

def draw_fibonacci_circles(n):
    fibo_seq = fibo(n)
    for i, num in enumerate(fibo_seq):
        turtle.penup()
        turtle.goto(i * 20, 0)  # Adjust spacing between circles
        turtle.pendown()
        draw_circle(num)

def main():
    turtle.speed(0)  # Set the speed to the fastest
    n = int(input('Enter the number of Fibonacci numbers to visualize: '))
    draw_fibonacci_circles(n)
    turtle.done()

if __name__ == "__main__":
    main()
