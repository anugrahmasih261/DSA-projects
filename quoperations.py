from Queue import Queue

q = Queue()
choice = 0

while choice != 5:
    print('All queue operations')
    print('Enter 1 to add elements to queue')
    print('Enter 2 to delete elements from queue')
    print('Enter 3 to search elements from queue')
    print("Enter 4 to display queue")
    print("Enter 5 to exit")

    choice = int(input('Enter your choice here: '))
    
    if choice == 1:
        element = input('Enter element: ')
        q.add(element)
        print('Your queue looks like this:', q.display())

    elif choice == 2:
        deleted_value = q.delete()
        if deleted_value != -1:
            print('Deleted element:', deleted_value)
            print('Your queue looks like this:', q.display())

        else:
            print('Queue Underflow')
    elif choice == 3:
        element = input('Enter an element for searching in the queue: ')
        result = q.search(element)
        print('Your queue looks like this:', q.display())

        if result != -1:
            print('Element found at position:', result)
        elif result == -2:
            print('Element not found in the Queue')
        else:
            print('Queue is empty')
    elif choice == 4:
        print('Your queue looks like this:', q.display())
    elif choice == 5:
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 5.')

print('Exiting the queue operations.')
