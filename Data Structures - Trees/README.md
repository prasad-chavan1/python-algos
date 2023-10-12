# Trees

A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges. Tree consists of many parent-child nodes. If each parent has at max two children nodes, it is called a Binary Tree. A tree where the parent has n number of children, such a tree is called a n-ary tree. The nodes at same level having same parent node are called sibings.

![Tree Data Structure](https://media.geeksforgeeks.org/wp-content/uploads/20221124153129/Treedatastructure.png)


### Properties associated with a Tree.

Root: The topmost node of a tree. <br>
Height of a tree: It is the length from the root to the deepest node.<br>
Degree of a Node: It is the number of child node that node has. <br>

### Types of trees:

1. General Tree
2. Binary Tree
3. Binary Search Tree
4. AVL Tree
5. Red Black Tree
6. N-ary Tree


## Binary Search Tree
The most used type of tree is Binary Search Tree or BST. BST allows us to quicky access a sorted list of numbers. BST being a binary tree follows the rule of having at max 2 child nodes at each parent level. Every BST node has a property that all the nodes in the left subtree are smaller in value than the root node and all the node of the right subtree are greater in value then the root node. Both subtrees of each node are also BSTs.

![Binary Search Tree](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221215114732/bst-21.png)

The BST has a average time complexity of ``O(log(n))`` for searching a number. The inorder traversal of a BST returns a sorted array.

The following code is for lookup for an element in a BST.

```python
def lookup(self,data):
    curr_node = self.root
    while True:
      if curr_node == None:
        return False
      if curr_node.data == data:
        return True
      elif data < curr_node.data:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
```

## Heap 

Heap data structure is a complete binary tree that satisfies the heap property, where any given node is 
- always greater than its child node/s and the key of the root node is the largest among all other nodes. This property is also called max heap property.
- always smaller than the child node/s and the key of the root node is the smallest among all other nodes. This property is also called min heap property.

Heapify is a process of creating a heap data structrue from a given binary tree.

Operations on a heap:
1. Insert into a heap
2. Delete from a heap
3. Peek in a heap (returns the maximum or minimum element from the heap)
4. Pop from a heap (returns the maximum or minimum element from the heap and remove that element)

![Heap Data Structure](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221220165711/MinHeapAndMaxHeap1.png)