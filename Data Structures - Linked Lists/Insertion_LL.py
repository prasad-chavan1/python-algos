class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0

            while current is not None and count < position - 1:
                current = current.next
                count += 1

            if current is None:
                print("Position out of range.")
                return

            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_position(1, 0)  # Insert 1 at position 0
    linked_list.insert_at_position(2, 1)  # Insert 2 at position 1
    linked_list.insert_at_position(3, 1)  # Insert 3 at position 1

    linked_list.display()  # Output: 1 -> 3 -> 2 -> None
