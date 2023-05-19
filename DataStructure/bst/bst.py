class TreeNode:
	def __init__(self, newItem, left, right):
		self.item = newItem
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.__root = None

	def search(self, x) -> TreeNode:
		return self.__searchItem(self.__root, x)
	
	def __searchItem(self, tNode:TreeNode, x) -> TreeNode:
		if (tNode == None):
			return None
		elif (x == tNode.item):
			return tNode
		elif (x < tNode.item):
			return self.__searchItem(tNode.left, x)
		else:
			return self.__searchItem(tNode.right, x)
		
	def insert(self, newItem):
		self.__root = self.__insertItem(self.__root, newItem)

	def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode:
		if (tNode == None):
			tNode = TreeNode(newItem, None, None)
		elif (newItem < tNode.item): # 그냥 진짜 삽입만 하는 함수
			tNode.left = self.__insertItem(tNode.left, newItem)
		else:
			tNode.right = self.__insertItem(tNode.right, newItem)
		return tNode
	
	def delete(self, x):
		self.__root = self.__deleteItem(self.__root, x)

	def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
		if (tNode == None):
			return None
		elif (x == tNode.item):
			tNode = self.__deleteNode(tNode)
		elif (x < tNode.item):
			tNode.left = self.__deleteItem(tNode.left, x)
		else:
			tNode.right = self.__deleteItem(tNode.right, x)
		return tNode
        
	def __deleteNode(self, tNode:TreeNode) -> TreeNode:
		# 3가지 case
		# 	1. tNode가 리프 노드
		# 	2. tNode가 자식이 하나만 있음
		# 	3. tNode가 자식이 둘 있음
		if tNode.left == None and tNode.right == None: # case1 : 자식이 없음
			return None
		elif tNode.left == None: # case2 : 오른자식뿐
			return tNode.right
		elif tNode.right == None: # case2 : 왼자식뿐
			return tNode.left
		else: # case3 : 두 자식이 다 있음
			rtnItem, rtnNode = self.__deleteMinItem(tNode.right)
			tNode.item = rtnItem
			tNode.right = rtnNode
			return tNode
		
	def __deleteMinItem(self, tNode:TreeNode) -> tuple:
		if tNode.left == None:
			return tNode.item, tNode.right
		else:
			rtnItem, rtnNode = self.__deleteMinItem(tNode.left)
			tNode.left = rtnNode
			return rtnItem, tNode
		
	def getRoot(self):
		return self.__root
		
	def preOrder(self, tNode:TreeNode):
		if (tNode != None):
			tNode.visited = True
			print(tNode.item, end=" ")
			self.preOrder(tNode.left)
			self.preOrder(tNode.right)

	def inOrder(self, tNode:TreeNode):
		if (tNode != None):
			self.inOrder(tNode.left)
			tNode.visited = True
			print(tNode.item, end=" ")
			self.inOrder(tNode.right)

	def postOrder(self, tNode:TreeNode):
		if (tNode != None):
			self.postOrder(tNode.left)
			self.postOrder(tNode.right)
			tNode.visited = True
			print(tNode.item, end=" ")

	def isEmpty(self) -> bool:
		return self.__root == self.NIL
	
	def clear(self):
		self.__root = self.NIL


bst1 = BinarySearchTree()
bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(80)
bst1.insert(90)
bst1.insert(7550)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)
bst1.delete(7550)
bst1.delete(10)

print("preorder")
bst1.preOrder(bst1.getRoot())
print("\ninorder")
bst1.inOrder(bst1.getRoot())
print("\npostorder")
bst1.postOrder(bst1.getRoot())
print("\n")