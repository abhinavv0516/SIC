class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

def insert_front(head):
    data = int(input("Enter data: "))
    new_node = Node(data)
    new_node.link = head
    return new_node

def insert_rear(head):
    data = int(input("Enter data: "))
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.link:
        current = current.link
    current.link = new_node
    return head

def delete_front(head):
    if head is None:
        print("Linked List is empty.")
        return None
    print(f"Element deleted: {head.data}")
    return head.link

def delete_end(head):
    if head is None:
        print("Linked List is empty.")
        return None

    if head.link is None:
        print(f"Element deleted: {head.data}")
        return None

    current = head
    while current.link.link:
        current = current.link
    print(f"Element deleted: {current.link.data}")
    current.link = None
    return head

def insert_at_pos(head):
    pos = int(input("Enter the position: "))
    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.link

    if pos < 1 or pos > cnt + 1:
        print("Insertion not possible.")
        return head

    if pos == 1:
        return insert_front(head)
    elif pos == cnt + 1:
        return insert_rear(head)

    data = int(input("Enter value for data: "))
    new_node = Node(data)
    
    current = head
    for _ in range(pos - 2):
        current = current.link

    new_node.link = current.link
    current.link = new_node
    return head

def delete_at_pos(head):
    if head is None:
        print("Linked List is empty.")
        return head

    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.link

    pos = int(input("Enter position to delete: "))

    if pos < 1 or pos > cnt:
        print("Invalid position.")
        return head

    if pos == 1:
        return delete_front(head)

    current = head
    for _ in range(pos - 2):
        current = current.link

    to_delete = current.link
    current.link = to_delete.link
    print(f"Element deleted: {to_delete.data}")
    return head

def display(head):
    if head is None:
        print("Linked List is empty.")
        return

    print("Contents of the Linked List:")
    current = head
    while current:
        print(current.data)
        current = current.link

def display_reverse(head):
    if head is None:
        return
    display_reverse(head.link)  
    print(head.data)

def menu():
    head = None

    while True:
        print("\n1. Insert front\n2. Insert rear\n3. Insert at position\n4. Display\n5. Delete at position\n6. Display Reverse\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            head = insert_front(head)
        elif choice == 2:
            head = insert_rear(head)
        elif choice == 3:
            head = insert_at_pos(head)
        elif choice == 4:
            display(head)
        elif choice == 5:
            head = delete_at_pos(head)
        elif choice == 6:
            display_reverse(head)
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
