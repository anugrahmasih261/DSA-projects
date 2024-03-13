from  Stack import*
s = Stack()
choice = 0

while choice <=5:
    print('All stack operations')
    print('Enter 1 to push elements to stack')
    print('Enter 2 to pop elements from stack')
    print('Enter 3 to peep elements from stack')
    print('Enter 4 to search elements from stack')
    print("enter 5 to exit")

    choice = int(input('Enter your choice here'))
    if choice ==1:
        element = input('Enter element')
        s.push(element)

    elif choice == 2:
        try:    
            popped_value=s.pop()
            print('The value of the popped element is',popped_value)
        except IndexError as e:
            print('Stack Underflow')
            
    elif choice==3:
        try:
            top_value=s.peep()
            print('The topmost element is ',top_value)
        except IndexError as e :
            print('Stack Empty')
        
    elif choice==4:
        element = input('Enter an element for    searching in the stack')
        result = s.search(element)
        if result != -1:
            print('Element found at position',result+1)
        else:
            print('Element not found in the Stack')
    elif choice ==5:
        break

print('Your stack looks like this',s.display())
