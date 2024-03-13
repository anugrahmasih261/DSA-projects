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


q = Dqueue()
choice = 0

while choice != 5:
    print('All deque operations')
    print('Enter 1 to add elements to front of deque')
    print('Enter 2 to add elements to rear of deque')
    print('Enter 3 to delete elements from front of deque')
    print('Enter 4 to delete elements from rear of deque')
    print('Enter 5 to search elements from deque')
    print("Enter 6 to display deque")
    print("Enter 7 to exit")

    choice = int(input('Enter your choice here: '))

    if choice == 1:
        element = input('Enter element to add to front: ')
        q.add_front(element)
        print('Your deque looks like this:', q.display())

    elif choice == 2:
        element = input('Enter element to add to rear: ')
        q.add_rear(element)
        print('Your deque looks like this:', q.display())

    elif choice == 3:
        deleted_value = q.delete_front()
        if deleted_value != -1:
            print('Deleted element from front:', deleted_value)
            print('Your deque looks like this:', q.display())
        else:
            print('Deque Underflow')

    elif choice == 4:
        deleted_value = q.delete_rear()
        if deleted_value != -1:
            print('Deleted element from rear:', deleted_value)
            print('Your deque looks like this:', q.display())
        else:
            print('Deque Underflow')

    elif choice == 5:
        element = input('Enter an element to search in the deque: ')
        result = q.search(element)
        if result != -1:
            print('Element found at position:', result)
        elif result == -2:
            print('Element not found in the Deque')
        else:
            print('Deque is empty')

    elif choice == 6:
        print('Your deque looks like this:', q.display())

    elif choice == 7:
        break

    else:
        print('Invalid choice. Please enter a number between 1 and 7.')

print('Exiting the deque operations.')
