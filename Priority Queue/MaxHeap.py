class MaxHeap:
    def __init__(self):
      self.heapList = []
      self.size = 0

    def getParent(self, index):
      return (index - 1) // 2
    
    def getLeftChild(self, index):
      return 2 * index + 1

    def getRightChild(self, index):
      return 2 * index + 2

    def getMax(self):
      return self.heapList[0]

    def remove(self, data):
        #TODO: implement remove
        pass

    def poll(self):
        tempRoot = self.heapList[0]
        self.heapList[0] = self.heapList.pop()
        self.size -= 1
        self.heapifyDown()
        return tempRoot

    def insert(self, data):
      self.heapList.append(data)
      self.size += 1 
      self.heapifyUp()

    def heapifyUp(self):
      currIndex = self.size - 1
      while currIndex > 0:
        parentIndex = self.getParent(currIndex)
        if self.heapList[currIndex] > self.heapList[parentIndex]:
          self.heapList[currIndex], self.heapList[parentIndex] = self.heapList[parentIndex], self.heapList[currIndex]
          currIndex = parentIndex

    def heapifyDown(self):
      currIndex = 0
      while currIndex < self.size:
          leftChildIndex = self.getLeftChild(currIndex)
          rightChildIndex = self.getRightChild(currIndex)
          # need to check is leftChildIndex and rightChildIndex are less than size because the right and child index for the last level in the heap will be out of bounds
          if leftChildIndex < self.size and self.heapList[currIndex] < self.heapList[leftChildIndex]:
              self.heapList[currIndex], self.heapList[leftChildIndex] = self.heapList[leftChildIndex], self.heapList[currIndex]
          if rightChildIndex < self.size and  self.heapList[currIndex] < self.heapList[rightChildIndex]:
              self.heapList[currIndex], self.heapList[rightChildIndex] = self.heapList[rightChildIndex], self.heapList[currIndex]
          currIndex += 1

    def heapifyUpRecursive(self, currIndex=None):
      if currIndex == 0:
        return

      if currIndex == None:
        currIndex = self.size - 1

      if self.heapList[currIndex] > self.heapList[self.getParent(currIndex)]:
          temp = self.heapList[currIndex]
          self.heapList[currIndex] = self.heapList[self.getParent(currIndex)]
          self.heapList[self.getParent(currIndex)] = temp
          self.heapifyUpRecursive(self.getParent(currIndex))

if __name__ == "__main__":
    # driver code
    heap = MaxHeap()
    for i in range(5):
        heap.insert(i)
    heap.insert(10)
    print(heap.heapList)
    heap.poll()
    print(heap.heapList)

    