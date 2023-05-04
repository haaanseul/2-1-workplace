from LinkedListBasic import LinkedListBasic


class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()
        
    def push(self, newItem):
        self.__list.insert(0, newItem)
        
    def pop(self):
        return self.__list.pop(0)
    
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.get(0)
        
    def isEmpty(self):
        return self.__list.isEmpty()
    
    def size(self):
        return self.__list.__sizeof__()
    
    def popAll(self):
        self.__list.clear()
        