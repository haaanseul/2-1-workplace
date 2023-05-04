from LinkedStack import *

class twoStackQueue:
    def __init__(self):
        self.__s = LinkedStack()
        self.__ts = LinkedStack()

    def moveelements(self, s, ts):
        while(not s.isEmpty()):
            ts.push(s.pop())

    def enqueue(self, x):
        self.moveelements(self.__s, self.__ts)
        self.__ts.push(x)
        self.moveelements(self.__ts, self.__s)

    def dequeue(self):
        return self.__s.pop()