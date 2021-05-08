class Node:
	def __init__(self):
		self.value=None
		self.right=None
		self.left=None
		self.parent=None
		self.height=None
		self.balance=None

class AVL:
	def __init__(self):
		self.root=None
		

	def insert(self,x):
		if self.root is None:
			self.root=Node()
			self.root.value=x
			self.root.height=0
			self.root.balance=0
			return

		current=self.root
		while True:
			if (x<=current.value):
				if (current.left is None):
					current.left=Node()
					current.left.value=x
					current.left.parent=current
					current.left.height=0
					current.left.balance=0
					self.update_balances(current.left)
					return
				else:
					current=current.left
			else:
				if (current.right is None):
					current.right=Node()
					current.right.value=x
					current.right.parent=current
					current.right.height=0
					current.right.balance=0
					self.update_balances(current.right)
					return

				else:
					current=current.right

	def update_heights(self,current):
		if (current is not None):
			if self.is_leaf(current):
				current.height=0
			elif (current.left is None):
				current.height=current.right.height+1
			elif (current.right is None):
				current.height=current.left.height+1
			else:
				current.height=max(current.left.height,current.right.height)+1
			current=current.parent
			self.update_heights(current)

	def is_leaf(self,current):
		if (current.left is None):
			if(current.right is None):
				print("hey")
				return True
		else:
			return False

	def update_balances(self,current):
		if current.balance>1 or current.balance<-1 :
				self.rotation(current)
				return

		if current.parent is not None:
			if (current.parent.left ==current):
				current.parent.balance+=1
			elif(current.parent.right==current):
				current.parent.balance-=1
			if(current.parent.balance!=0):
				self.update_balances(current.parent)
		
		

	def rotation(self,current):
		if current.balance<0:
			if current.right.balance>0:
				self.rotate_right(current.right)
				self.rotate_left(current)
			else:
				self.rotate_left(current)
		elif(current.balance>0):
			if current.left.balance<0:
				self.rotate_left(current.left)
				self.rotate_right(current)
			else:
				self.rotate_right(current)
		

	def rotate_right(self,z):
		#right rotate........
		y=z.left
		t=y.right
		z.left=t
		if t is not None:
			t.parent=z

		if z.parent is None:
			self.root=y
		else:
			if (z.parent.left is z):
				z.parent.left=y
			else:
				z.parent.right=y
		y.right=z
		z.parent=y

		z.balance=z.balance-1-max(0,y.balance)
		y.balance=y.balance-1+min(0,z.balance)
		

	def rotate_left(self,z):
		#left rotate..........
		y=z.right
		t=y.left
		z.right=t
		if t is not None:
			t.parent=z

		if z.parent is None:
			self.root=y
		else:
			if (z.parent.left is z):
				z.parent.left=y
			else:
				z.parent.right=y
		y.left=z
		z.parent=y
		
		z.balance=z.balance+1-min(y.balance,0)
		y.balance=y.balance+1+max(z.balance,0)



	def print_tree(self,current):
		if (current.left):
			self.print_tree(current.left)
		print(current.value)

		if (current.right):
			self.print_tree(current.right)

	def search(self,x):
		if (self.root==x):
			print("Element found at root")
			return self.root
		else:
			current=self.root
			while True:
				if(x<current.value):
					if(current.left):
						current=current.left
					else:
						print("Element not present")
						return None
				elif(x>current.value):
					if(current.right):
						current=current.right
					else:
						print("Element not present")
						return None
				elif(x==current.value):
					print("Element found")
					return current
	def minimum(self,current):
		while(current is not None):
			prev=current
			current=current.left
		return(prev.value)

	def maximum(self,current):
		while(current is not None):
			prev=current
			current=current.right
		return(prev.value)

	def successor(self,x):
		current=self.search(x)
		if self.maximum(self.root)==x:
			print("No successor")
			return
		if current.right !=None:
			print(self.minimum(current.right))
			return
		y=current.parent
		while(y!=None and current==y.right):
			current=y
			y=y.parent

		print(y.value)

	def predecessor(self,x):
		current=self.search(x)
		if self.minimum(self.root)==x:
			print("No predecessor")
			return
		if current.left !=None:
			print(self.maximum(current.left))
			return
		y=current.parent
		while(y!=None and current==y.left):
			current=y
			y=y.parent

		print(y.value)
	def delete(self,x):
		if (self.root==x):
			current=self.root
		else:
			current=self.root
			while True:
				if(x<current.value):
					if(current.left):
						current=current.left
					else:
						print("Element not present")
						return
				elif(x>current.value):
					if(current.right):
						current=current.right
					else:
						print("Element not present")
						return
				elif(x==current.value):
					z=current
					break

		if (z.left==None):
			self.transplant(z,z.right)
		elif(z.right==None):
			self.transplant(z,z.left)
		else:
			current=z.right
			while(current is not None):
				prev=current
				current=current.left
			y=prev
			if (y.parent is not None):
				self.transplant(y,y.right)
				y.right=z.right
				y.right.parent=y
			self.transplant(z,y)
			y.left=z.left
			y.left.parent=y
		self.update_balances(current)


	def transplant(self,u,v):
		if (u.parent is None):
			self.root=v
		elif(u==u.parent.left):
			u.parent.left=v
		else:
			u.parent.right=v
		if (v is not None):
			v.parent=u.parent



	



def main():
	a=AVL()
	a.insert(0)
	a.insert(1)
	a.insert(4)
	a.insert(5)
	a.print_tree(a.root)
	a.delete(4)
	a.print_tree(a.root)

if __name__=='__main__':
	main()
