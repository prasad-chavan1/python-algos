# Stacks and Queues

In computer science, **stacks** and **queues** are fundamental data structures that play a crucial role in managing and manipulating data. In this README, we will explore these data structures and provide implementations for each of them.

## Stacks

A **stack** is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It can be thought of as a collection of elements with two main operations:

1. **Push:** Adds an element to the top of the stack.
2. **Pop:** Removes and returns the top element from the stack.

![Stack working](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221219100314/stack.drawio2.png)
### Stacks using Arrays

One common way to implement a stack is by using arrays. This implementation provides a fixed-size stack and is relatively straightforward to implement. Here's a basic example of how to create a stack using arrays:

```python
class StackUsingArray:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
```
## Stacks using Linked List
Another way to implement a stack is by using a linked list. This implementation allows for dynamic memory allocation and can handle an arbitrary number of elements. Here's an example of how to create a stack using a linked list:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item

    def is_empty(self):
        return self.top is None
```
## Queues

A queue is another linear data structure that follows the First-In-First-Out (FIFO) principle. It is commonly used for tasks like managing tasks in a printer queue or handling requests in web servers. The primary operations on a queue are:

Enqueue: Adds an element to the back of the queue. <br />
Dequeue: Removes and returns the front element from the queue.<br />
![Queue Working](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221213113312/Queue-Data-Structures.png)

## Queues using Linked List
Implementing a queue using a linked list provides flexibility and dynamic memory allocation. Here's an example of how to create a queue using a linked list:
``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.data
            self.front = self.front.next
            if not self.front:
                self.rear = None
            return removed_item

    def is_empty(self):
        return self.front is None
```
This detailed `README.md` provides information about stacks and queues.
