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

    def insert(self, value, priority):
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

    def remove(self):
        if self.is_empty():
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.value
        
