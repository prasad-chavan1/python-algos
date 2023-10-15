# Graphs in Python

This repository contains Python code and explanations related to graphs and their fundamental operations such as Breadth-First Search (BFS), Depth-First Search (DFS), and graph implementation.

## Table of Contents

- [Introduction to Graphs](#introduction-to-graphs)
- [Graph Implementation](#graph-implementation)
- [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Depth-First Search (DFS)](#depth-first-search-dfs)


## Introduction to Graphs

A graph is a fundamental data structure that represents a collection of nodes (vertices) connected by edges. Graphs are used to model relationships between objects and can be found in various real-world scenarios, such as social networks, transportation systems, and computer networks.

### Graph Types

There are various types of graphs, including:

- **Directed Graph (Digraph)**: Edges have a direction.
- **Undirected Graph**: Edges have no direction.
- **Weighted Graph**: Edges have associated weights.
- **Unweighted Graph**: Edges have no weights.
- **Cyclic Graph**: Contains at least one cycle.
- **Acyclic Graph**: Contains no cycles.

## Graph Implementation

In this repository, we provide a Python implementation of a graph data structure. This implementation allows you to create, manipulate, and traverse various types of graphs.

### Supported Operations

- Create an empty graph.
- Add vertices and edges.
- Remove vertices and edges.
- Check if a vertex or edge exists.
- Perform graph traversal (BFS and DFS).
- Calculate graph properties (e.g., connected components).

```python
from graph import Graph

# Create an instance of a graph
my_graph = Graph()

# Add vertices
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

# Add edges
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'D')
my_graph.add_edge('D', 'A')

# Check if an edge exists
if my_graph.has_edge('A', 'B'):
    print("Edge A -> B exists")

# Perform BFS traversal
bfs_result = my_graph.breadth_first_search('A')
print("BFS Traversal:", bfs_result)

# Perform DFS traversal
dfs_result = my_graph.depth_first_search('A')
print("DFS Traversal:", dfs_result)
```
## Breadth-First Search (BFS)

Breadth-First Search is a graph traversal algorithm that explores all the vertices at the current level before moving to the next level. It's often used to find the shortest path in unweighted graphs.

``` python
# Perform BFS traversal
bfs_result = my_graph.breadth_first_search('A')
print("BFS Traversal:", bfs_result)
```
## Depth-First Search (DFS)

Depth-First Search is another graph traversal algorithm that explores as far as possible along each branch before backtracking. It's used for tasks like topological sorting and cycle detection.

``` python
# Perform DFS traversal
dfs_result = my_graph.depth_first_search('A')
print("DFS Traversal:", dfs_result)
```
