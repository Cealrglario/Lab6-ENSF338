import random
import timeit
import sys

sys.setrecursionlimit(15000)

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        if self.is_empty() or self.head.priority > priority: # a greater priority value means a LOWER priority in the queue
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None and temp.next.priority < priority: # enqueue at tail, dequeue at head
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.value
        
class Heap:

    def __init__(self):
        self.arr = []

    def heapify(self, new_arr):
        self.arr = new_arr
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.do_heapify(i)

    def enqueue(self, new_element, priority):
        self.arr.append((priority, new_element))
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.do_heapify(i)

    def dequeue(self):
        if len(self.arr) == 0:
            return None 
        data = self.arr.pop(0)[1]  # Return only the value, not the priority
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.do_heapify(i)
        return data

    def do_heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.arr) and self.arr[left][0] > self.arr[largest][0]:  # Compare priorities, not values
            largest = left

        if right < len(self.arr) and self.arr[right][0] > self.arr[largest][0]:  # Compare priorities, not values
            largest = right

        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self.do_heapify(largest)

tasks = []
for _ in range(1000):
    if random.random() < 0.7:
        tasks.append(('enqueue', random.randint(1, 10)))  # Enqueue a random integer between 1 and 10
    else:
        tasks.append('dequeue')

# Create instances of PriorityQueue and Heap
pq = PriorityQueue()
heap = Heap()

# Define functions to process tasks for each implementation
def process_tasks_pq(tasks):
    for task in tasks:
        if task == 'dequeue':
            pq.dequeue()
        else:
            pq.enqueue(task[1], task[1])  # Use the value as the priority

def process_tasks_heap(tasks):
    for task in tasks:
        if task == 'dequeue':
            heap.dequeue()
        else:
            heap.enqueue(task[1], task[1])  # Use the value as the priority

# Measure the time it takes to process the tasks for each implementation
start_time = timeit.default_timer()
process_tasks_pq(tasks)
pq_time = timeit.default_timer() - start_time

start_time = timeit.default_timer()
process_tasks_heap(tasks)
heap_time = timeit.default_timer() - start_time

# Print the overall time and average time per task for each implementation
print(f"\nPriorityLinkedList: Overall time = {pq_time} seconds, Average time per task = {pq_time / len(tasks)} seconds\n")
print(f"PriorityHeap: Overall time = {heap_time} seconds, Average time per task = {heap_time / len(tasks)} seconds\n")

'''
Q4) The Priority Queue LinkedList implementation is faster than the Priority Queue Heap implementation by approximately a factor of 15. The reason for this is due to the nature of dequeueing with linked lists vs. the PriorityHeap. 
With the linked list, dequeueing is a constant time operation, O(1), because the head of the list is always the next element to be dequeued. With the PriorityHeap, dequeueing is a logarithmic time operation O(log n). This is because 
the heap must maintain its shape and order, and the root of the heap must be the element with the highest priority. And so while it is true that there were more enqueue operations than dequeue ones, the fact that dequeue was O(1) for
linked lists and O(log n) for heaps is likely what made the difference in execution time. Therefore, the PriorityLinkedList was faster than the PriorityHeap. 
'''