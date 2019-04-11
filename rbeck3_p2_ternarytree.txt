# Ryan Beck | MCS 275 | Project 2 | 11.16.18
# Ternary Tree


class Tree(object):

	def __init__(self, value):
		self.value = value
		self.left = None
		self.middle = None
		self.right = None

	def insert_node(self, new_value):
		if new_value < self.value:
			if self.left == None:
				self.left = Tree(new_value)
			else:
				self.left.insert_node(new_value)
		elif new_value == self.value:
			if self.middle == None:
				self.middle = Tree(new_value)
			else:
				self.middle.insert_node(new_value)
		else: 
			if self.right == None:
				self.right = Tree(new_value)
			else:
				self.right.insert_node(new_value)

	def preorder_traversal(self):
		print(self.value)
		if self.left != None:
			self.left.preorder_traversal()
		if self.middle != None:
			self.middle.preorder_traversal()
		if self.right != None:
			self.right.preorder_traversal()

	def inorder_traversal(self):
		if self.left != None:
			self.left.inorder_traversal()
		if self.middle != None:
			self.middle.inorder_traversal()	
		print(self.value)
		if self.right != None:
			self.right.inorder_traversal()

	def postorder_traversal(self):
		if self.left != None:
			self.left.postorder_traversal()
		if self.middle != None:
			self.middle.postorder_traversal()
		if self.right != None:
			self.right.postorder_traversal()
		print(self.value)

def construct_ternary_tree(L):
	T = Tree(L[0])
	for value in L[1:]:
		T.insert_node(value)
	return T

def main():

	L = [4,1,2,2,3,1,0,4,6,5,6,4]
	T = construct_ternary_tree(L)
	print('preorder traversal: depth-first')
	T.preorder_traversal()
	print('inorder traversal')
	T.inorder_traversal()
	print('postorder traversal: breadth-first')
	T.postorder_traversal()

main()