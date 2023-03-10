'''Breadth-first search is an algorithm for finding an element in a tree or graph. 
BFS starts by checking the root node, then it checks all of the elements that are 1 edge 
away from the root node, then all of the elements 2 edges away, and so on until the desired 
element is found or the entire graph is traversed. It accomplishes this by building a 
first-in first-out queue of elements to check. As each element is checked, its children 
are added to the end of the queue so that the entire graph is traversed layer by layer.'''

def breadth_first_search(root_node, fn):
    # Returns the first node for which fn(node) is truthy
    queue = deque([root_node]) # Python queue object
    while len(queue) > 0:
        node = queue.popleft() # Grab the first element in queue
        if fn(node.value):
            return node
        else:
            # (Fill in the missing line here)
            queue.extend(node.children)
    return None
