from heap import *

A = Heap()

A.insert([1,3])
A.insert([2,5])
A.insert([3,3])
A.insert([4,1])
A.insert([5,2])
A.insert([6,2])
A.insert([7,1])
A.insert([8,4])

A.plus_freq(3)

A.printHeap()