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
