from collections import deque

'''
--------------- BFS --------------------
-> Time Complexity - O(N) + O(2E) where, N - number of node, E - number of edges
-> This works for both directed and undirected graphs
----------------------------------------
'''

# graph - an adjacency list graph, the graph is 0 indexed
# node - the starting node of the traversal
def bfs_helper(graph, node, visited):

	q = deque()
	bfs = [] # list to store the traversal

	# add the starting node
	q.append(node)

	while q: # while the queue is not empty

		node = q.popleft()
		bfs.append(node)
		visited[node] = 1 # mark as visited
		# for each of its neighbours
		for neighbour in graph[node]:
			if visited[neighbour]!=1: # if not visited
				q.append(neighbour)

	return bfs 

def bfs(graph):

    n = len(graph) # number of nodes in graph
    visited = [0 for i in range(n)]
    all_traversals = [] # holds the list of all traversals for all connected components

    for node in range(n):
        if visited[node]==0:
            bfs = bfs_helper(graph, node, visited)
            all_traversals.append(bfs)

    return all_traversals 

