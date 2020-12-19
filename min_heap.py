# Course: CS261 - Data Structures
# Assignment: 5
# Student: Dan Glendon
# Description: Portfolio minimum heap implementation


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds given object to the minimum heap, then percolates it to the proper location
        """
        self.heap.append(node)
        l = self.heap.length()-1
        while l != 0:
            j = (l-1)//2 # parent is always located at (index - 1) / 2 floored
            if self.heap.get_at_index(l) < self.heap.get_at_index(j):
                self.heap.swap(l, j)
                l = j
            else:
                break

    def get_min(self) -> object:
        """
        Returns the minimum value in the minheap, which is always at index 0
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes the minimum value from the minheap and re-heapifies the heap
        """
        if self.is_empty():
            raise MinHeapException
        value = self.heap.get_at_index(0)
        self.heap.set_at_index(0, self.heap.get_at_index(self.heap.length()-1))
        index = 0
        self.heap.pop()
        while index != self.heap.length()-1:
            left, right = None, None
            if 2*index+1 > self.heap.length()-1 and 2*index+2 > self.heap.length()-1:
                break
            if 2*index+1 <= self.heap.length()-1:
                left = self.heap.get_at_index(2*index+1)
            if 2*index+2 <= self.heap.length()-1:
                right = self.heap.get_at_index(2*index+2)
            node = self.heap.get_at_index(index)
            if left is None and right is None:
                break
            elif left is None and right is not None:
                if node < right:
                    break
                else:
                    self.heap.swap(index, 2*index+2)
                    index = 2*index+2
            elif right is None and left is not None:
                if node < left:
                    break
                else:
                    self.heap.swap(index, 2*index+1)
                    index = 2*index+1
            elif left > right:
                self.heap.swap(index, 2*index+2)
                index = 2*index+2
            else:
                self.heap.swap(index, 2*index+1)
                index = 2*index+1
        return value

    def build_heap(self, da: DynamicArray) -> None:
        """
        Turns an existing array into a proper min heap
        """
        self.heap = DynamicArray()
        for x in range(da.length()):
            self.heap.append(da.get_at_index(x))
        for x in range(self.heap.length()-1, -1, -1):
            y = x
            done = False
            if 2*y+1 <= self.heap.length()-1 and 2*y+2 <= self.heap.length()-1:
                while True:
                    left, right, swapper = None, None, None
                    try:
                        left = self.heap.get_at_index(2*y+1)
                    except IndexError:
                        pass
                    try:
                        right = self.heap.get_at_index(2*y+2)
                    except IndexError:
                        pass
                    node = self.heap.get_at_index(y)
                    if left is None and right is None:
                        break
                    elif left is None:
                        swapper = 2*y+2
                    elif right is None:
                        swapper = 2*y+1
                    elif node <= left and node <= right:
                        break
                    elif left > right:
                        swapper = 2*y+2
                    else:
                        swapper = 2*y+1
                    if swapper is not None:
                        self.heap.swap(y, swapper)
                        y = swapper




# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
