import random

class Heap:

    def __init__(self):
        self.arr = []

    def heapify(self, new_arr):
        self.arr = new_arr
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.do_heapify(i)

    def enqueue(self, new_element):
        self.arr.append(new_element)
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.do_heapify(i)

    def dequeue(self):
        data = self.arr.pop(0)
        for i in range(len(self.arr) // 2 - 1, -1, -1):
            self.do_heapify(i)

    def do_heapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.arr) and self.arr[left] > self.arr[largest]:
            largest = left

        if right < len(self.arr) and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self.do_heapify(largest)

# array is already heap
heap = Heap()
heap.heapify([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(heap.arr == [9, 8, 7, 6, 5, 4, 3, 2, 1])

# array is empty
heap = Heap()
heap.heapify([])
print(heap.arr == [])

# array is a long, random array
heap = Heap()
heap.heapify([1, 2, 8, 4, 8, 5, 2, 3, 5, 3, 3, 8, 5, 7, 9, 3])
print(heap.arr == [9, 8, 8, 5, 3, 5, 8, 3, 4, 2, 3, 1, 5, 7, 2, 3])
