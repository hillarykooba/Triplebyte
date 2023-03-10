'''
This merge routine is very useful in sorting algorithms, most famously in merge sort. The key idea is to take the smallest element in each list, add the smaller of those two values to an output list, and discard that element from further consideration. The real genius is that, because the two lists are already sorted, we can merge them together in linear time. We can compare the first element of each list, pop off the smaller value, and add it to an output list, continuing until both lists are empty. This approach works well for merging 2 lists, but does not extend well to larger numbers of lists. However, a heap data structure is able to merge k lists with n total items in O(k log n) time.
'''

def merge(list1, list2):
    # Takes two sorted lists and merges them in sorted order
    i1 = i2 = 0
    out_list = []
    # (Fill in the missing line here)
    while i1 < len(list1) or i2 < len(list2):
        elem1 = list1[i1] if i1 < len(list1) else None
        elem2 = list2[i2] if i2 < len(list2) else None
        if elem1 is None or (elem2 is not None and elem2 < elem1):
            out_list.append(elem2)
            i2 += 1
        else:
            out_list.append(elem1)
            i1 += 1
    return out_list
  
  # Answer: while i1 < len(list1) or i2 < len(list2):
