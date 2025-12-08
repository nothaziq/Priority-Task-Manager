class PriorityQueue:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

    def getAllTasks(self):
        return self.heap.copy()
    
    def insert(self, task):
        self.heap.append(task)
        self.heapifyUp(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return  None

        if len(self.heap)==1:
            return self.heap.pop()

        min_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_task

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]


    def heapifyUp(self, index):
        parentIndex = (index - 1) // 2

        if index> 0 and self.heap[index]['priority'] < self.heap[parentIndex]['priority']:
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            self.heapifyUp(parentIndex)

    def heapifyDown(self, index):

        smallest = index
        leftChild = 2* index + 1
        rightChild = 2* index + 2

        if leftChild <len(self.heap) and self.heap [leftChild]['priority'] < self.heap[smallest]['priority']:
            smallest = leftChild

        if rightChild <len(self.heap) and self.heap[rightChild]['priority'] < self.heap[smallest]['priority']:
            smallest = rightChild 

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapifyDown(smallest)


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def getAllTasks(self):
        return self.items.copy()