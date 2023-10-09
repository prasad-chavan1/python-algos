'''
Reference : https://www.geeksforgeeks.org/deletion-in-linked-list/
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_node(self, key):
        current = self.head

        # If the key to be deleted is the head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found in the list
        if current is None:
            print(f"{key} not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Original Linked List:")
    linked_list.display()

    key_to_delete = 3
    linked_list.delete_node(key_to_delete)

    print(f"Linked List after deleting {key_to_delete}:")
    linked_list.display()
