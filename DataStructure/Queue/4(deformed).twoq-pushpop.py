from linkedQueue import *


class TwoQueueStack:
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()

    def __move_elements(self, q, tq):
        while not q.isEmpty():
            tq.enqueue(q.dequeue())

    def push(self, x):
        self.__q.enqueue(x)

    def pop(self):
        self.__move_elements(self.__q, self.__tq)
        while(self.__tq.size() > 1):
            self.__q.enqueue(self.__tq.dequeue())
        return self.__tq.dequeue()
    
    def printq(self):
        self.__q.printQueue()

