class BidirectNode:
    def __init__(self, key, value, prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.key = key
        self.value = value
        self.prev = prevNode
        self.next = nextNode