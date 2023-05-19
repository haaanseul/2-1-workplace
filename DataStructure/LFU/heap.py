class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []
    
    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A) - 1)
    
    def __percolateUp(self, i):
        parent = (i-1) // 2
        if i > 0 and self.__A[i][1] < self.__A[parent][1]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)
    
    def deleteMin(self):
        if not self.isEmpty():
            min = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return min
        else:
            return None
    
    def __percolateDown(self, i):
        child = 2 * i + 1
        right = 2 * i + 2
        if (child <= len(self.__A)-1):
            if right <= len(self.__A)-1 and self.__A[child][1] > self.__A[right][1]:
                child = right
            if self.__A[i][1] > self.__A[child][1]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
    
    def min(self):
        return self.__A[0]
    
    def isEmpty(self):
        return len(self.__A) == 0
    
    def clear(self):
        self.__A = []
        
    def size(self):
        return len(self.__A)
    
    def findidx(self, x): # 인덱스 찾기
        for i in range(len(self.__A)):
            if x == self.__A[i][0]:
                return i
        return None
    
    def plus_freq(self, x): # 빈도수 1 올리기
        idx = self.findidx(x)
        self.__A[idx][1] += 1
        self.__percolateDown(idx)