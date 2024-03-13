# All liked list operations 

link_list = []

link_list.append('America')
link_list.append('Japan')
link_list.append('India')
print('Existing link list is', link_list)
choice = 0

while choice <5:
    print('All linked list operations')
    print('Enter 1 to Add element')
    print('Enter 2 to Remove element')
    print('Enter 3 to Replace element')
    print('Enter 4 to Search element')
    print('Enter 5 to Exit')


    choice = int(input('enter your choice here to perform actions'))
    if choice == 1:
        element = input('enter elemet to add = ')
        pos = int(input('At what position would you like to add ='))
        link_list.insert(pos, element)
        print('new linked list after addition is', link_list)
        
    elif choice == 2 :
        try:
            element = input('enter element to remove =')
            link_list.remove(element)
            print('new linked list after addition is', link_list)

        except ValueError:
            print('element you wanted to remove does not exist')

    elif choice == 3:
        element = input('enter New element to Replace = ')
        pos = int(input('at what position you want to replace'))
        link_list.pop(pos)
        link_list.insert(pos, element)
        print('new linked list after addition is', link_list)

    elif choice ==4:
        element = input('enter element to search = ')
        try:
            pos = link_list.index(element)
            print('element found at position', pos)
            print('new linked list after addition is', link_list)
        except ValueError:
            print('Element does not exists in link list')
    
    elif choice ==5:
        break





