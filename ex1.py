import timeit
import sys

sys.setrecursionlimit(15000)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
sorted_list = list(range(10000))

bst = BST()

for element in sorted_list:
    bst.insert(element)

times = []
total_time = 0

for i in range(10000):
    time = timeit.timeit('bst.search(i)', globals=globals(), number=10)
    times.append(time)
    total_time += time

print("\nTotal time (linear BST insertion): ", total_time)
print("Average time per element (linear BST insertion): ", total_time/10000)

# Now we shuffle the list

import random
random.shuffle(sorted_list)
shuffled_list = sorted_list
bst = BST()

for element in shuffled_list:
    bst.insert(element)
    
times = []
total_time = 0

for i in range(10000):
    time = timeit.timeit('bst.search(i)', globals=globals(), number=10)
    times.append(time)
    total_time += time

print("Total time (shuffled BST insertion): ", total_time)
print("Average time per element (shuffled BST insertion): ", total_time/10000, '\n')

'''
Q4) Inserting a shuffled list into a BST is MUCH more efficient than inserting a sorted list. This is because when you insert a sorted list into a BST, it leads to the BST becoming skewed, 
in our case being skewed to the right due to our list being in increasing order. The first node only has a right node to the second node, the second node only has a right node to the third node, and so on.
This means that the time complexity of searching for an element in the BST becomes O(n) as it'd basically be akin to performing a linear seach on an array for an element. The reason that an unsorted list insertion is
more efficient is because the BST is more balanced, and the time complexity of searching for an element in the BST is virtually O(log n) as it'd be akin to performing a binary search on an array for an element. This is why
the total time and average time per element for the shuffled list is much lower than that of the sorted list.
'''