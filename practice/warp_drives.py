'''
BFS finds the shortest path on an unweighted graph, because it always explores the path with the fewest steps before it expends to paths with more steps. However, in a weighted graph, a path with more steps might be shorter than one with fewer. Dijkstra's algorithm fixes this problem. It's a best-first graph traversal. It looks a lot like BFS, but in place of a queue, it uses a priority queue. When a node is pushed onto the queue, it's given a priority equal to the length of the path to that node. Thus when a node is dequeued, the path that node represents will be the shortest unexplored path. If you want to get even more advanced, you can view the A graph search algorithm as an extension of Dijkstra's. It's just like Dijkstra's, but rather than using the path length alone as the priority in the best-first queue, it adds a heuristic that estimates how far a given node might be from the destination. As long as this heuristic satisfies certain constraints, A is still guaranteed to find the shortest path.
'''

Warp drives, as advanced as they are, don't allow teleportation. Your computer has just downloaded information on the travel time between connected warp stations. Which algorithm will find the path with the shortest travel time from Earth to TRAPPIST-1?

Select the correct answer:

Breadth first search will still find the path with the shortest travel time.


Topological sort will find the shortest path on any weighted network.


Dijkstra's algorithm extends BFS to weighted graphs.


Building a minimum spanning tree will efficiently find the shortest path between any two warp stations.

# Answer: Dijkstra's algorithm extends BFS to weighted graphs.
