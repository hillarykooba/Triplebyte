'''
Self-balancing Binary Search Trees take O(log n) worst-case time to insert or delete an item, even when it requires a rebalance operation. In comparison, sorted arrays take worst-case O(n) time to add or remove an item, which can be prohibitively expensive for large data structures. While arrays and trees both require O(n) memory, the constant factor of a tree is much greater because of the memory required for child pointers. Additionally, B-trees and B+ trees can be optimized on modern hardware, minimizing cache misses and disk reads to increase real-world performance.
'''

It's possible to use the binary search algorithm to find an element in a sorted array in O(log n) time. Binary search trees have this same search performance. Why, then, do we ever use more complicated binary search trees rather than sorted lists?

Select the correct answer:

BSTs are faster for finding the largest and smallest elements in a set.


BSTs require less memory than a sorted list.


BSTs have constant-time access to the median value in a list.


BSTs are faster for inserting and deleting items.

# Answer: BSTs are faster for inserting and deleting items.
