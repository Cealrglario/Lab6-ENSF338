import timeit
import random
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
    
def binary_search(arr, low, high, key): # reminder that low and high are indices, not values
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1
    
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1] # put the pivot in the middle
    return (i+1)

def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        part = partition(arr, low, high)
        quicksort(arr, low, part-1)
        quicksort(arr, part+1, high)

search_list = list(range(10000))
random.shuffle(search_list)

bst = BST()

for i in search_list:
    bst.insert(i)

times = []
total_time = 0

for i in range(10000):
    time = timeit.timeit('bst.search(i)', globals=globals(), number=10)
    times.append(time)
    total_time += time

print("\nTotal time for searching (BST): ", total_time)
print("Average time per element (BST): ", total_time/10000)

quicksort(search_list, 0, len(search_list)-1)

times = []
total_time = 0

for i in range(10000):
    time = timeit.timeit('binary_search(search_list, 0, len(search_list)-1, i)', globals=globals(), number=10)
    times.append(time)
    total_time += time

print("\nTotal time for searching (binary search on array): ", total_time)
print("Average time per element (binary search on array): ", total_time/10000, "\n")

'''
Q4) Both approaches are, virtually, equally as efficient. The average time to search each element is in the realm of 0.00001 seconds, and
the total time for searching all 10,000 elements is in the realm of 0.1 seconds. This is because searching for elements within a BST,
assuming that the elements within the BST are near balanced (if not balanced), which can occur with shuffled data, is of average
time complexity O(log n). This is the same average time complexity as searching a sorted array using binary search. Therefore,
both approaches are equally as efficient, and any minor differences in time are negligible and could be attributed to factors
other than the data structures and algorithms themselves.
'''