class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_intersection_node(head1, head2):
    nodes_set = set()

    # Traverse the first list and store the nodes in a set
    current = head1
    while current:
        nodes_set.add(current)
        current = current.next

    # Traverse the second list and check if any node is in the set
    current = head2
    while current:
        if current in nodes_set:
            return current
        current = current.next

    return None

# Example usage
if __name__ == "__main__":
    # Create two linked lists
    # List 1: 1 -> 2 -> 3 -> 4 -> 5
    # List 2:         8 -> 9 -> 4 -> 5
    common = Node(4)
    common.next = Node(5)

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = common

    head2 = Node(8)
    head2.next = Node(9)
    head2.next.next = common

    # Find the intersection node
    intersection = get_intersection_node(head1, head2)
    if intersection:
        print(f"The linked lists intersect at node with data: {intersection.data}")
    else:
        print("The linked lists do not intersect.")
