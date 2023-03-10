'''
Breadth-first search and depth-first search are the two most basic graph traversal algorithms. BFS explores nodes in expanding circles of distance from its start location, and thus will find the shortest path between two nodes (or star systems). DFS makes no such guarantee (indeed, it often finds pretty crazy, winding paths). One advantage of DFS, however, is that it uses much less memory. BFS must store a queue of nodes to visit, and this queue can grow to (order) the size of the entire graph. If you need to find the shortest path through a graph, but don't want to use linear memory, a cool algorithm is iterative deepening search. It's just like depth-first search, but takes a parameter that limits how deep to look. If we limit the depth to 5, say, it will do a depth-first exploration of all paths up to length 5. Imagine what happens, now, if we run the search multiple times, starting with a depth limit of 1, then 2, then 3, etc. Because this explores all paths of length N before it explores any of length N+1, it is guaranteed to find shortest paths. And because it's using depth-first traversal, it only uses O(log n) memory! This sounds really slow, you might think (it seems to be duplicating a lot of searching). However, consider the case of a roughly balanced binary tree. Half of all nodes will be found in the leaf level of the tree. And these nodes are only explored once. If we calculate the total number of times that nodes are traversed, we get N + N/2 + N/4... This sequence sums to 2N. Thus, iterative deepening search still takes linear time.
'''

The year is 20XX. The United Earth Federation has created a network of warp stations between distant star systems. Your mission, should you choose to accept it, is to hop across the galaxy and man the battlestation at the TRAPPIST-1 system. Your computer has a map of UEF warp stations and the routes that connect them. Which algorithm will help you get to your destination in the fewest number of warps?

Select the correct answer:

Depth first search is guaranteed to find the shortest path to TRAPPIST-1.


Breadth first search will find the shortest path to the battlestation, even if the network contains cycles.


Simulated annealing will minimize the number of warps with high probability.


Union-find algorithm is the only approach that can handle a network with cycles.

# Answer: Breadth first search will find the shortest path to the battlestation, even if the network contains cycles.
