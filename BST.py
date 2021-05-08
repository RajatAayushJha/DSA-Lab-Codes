class Node:
	def __init__(self,info,ancestor):
		self.info=info
		self.left=None
		self.right=None
		self.ancestor=ancestor

class BST:
	def __init__(self):
		self.root=None

	def __str__(self):
		return 

	def insert(self,x):
		if self.root==None:
			self.root=Node(x,None)
			return
		current=self.root
		while True:
			if x<current.info:
				current1=current
				if current.left:
					current1=current
					current=current.left
				else:
					current.left=Node(x,current1)
					return
			if x>current.info:
				current1=current
				if current.right:
					current1=current
					current=current.right
				else:
					current.right=Node(x,current1)
					return




def delete(root, key):
	z=find(root,key)
	if z:
		if z.left==None or z.right==None:
			y=z
		else:
			d=succe(key)
			y=find(root,d)
		if y.left!=None:
			x=y.left
		else:
			x=y.right
		if x!=None:
			x.ancestor=y.ancestor
		if y.ancestor==None:
			root.info=x
		elif y==y.ancestor.left:
			y.ancestor.left=x
		else:
			y.ancestor.right=x
		if y!=z:
			z.info=y.info
		return
	else :
		return print("Doesn't exist")






	

  
    
    
def find(root,x):
	if x in l:
		current=root
		while True:
			if x<current.info:
				current=current.left
			elif x>current.info:
				current=current.right
			else:
				return current

	return False





def preOrder(parent):
	if parent:
		print(parent.info,end=" ")
		preOrder(parent.left)
		preOrder(parent.right)


def Search(parent,x):
	if parent:
		if x<parent.info:
			Search(parent.left,x)
		elif x==parent.info:
			return print("True")
		else :
			Search(parent.right,x)

	else :
		return print("False")

def minimum(parent):
	current=parent
	while True:
		if current.left:
			current=current.left
		else:
			return current.info

def maximum(parent):
	current=parent
	while True:
		if current.right:
			current=current.right
		else:
			return current.info


l=[]
def inOrder(parent):
	if parent:
		inOrder(parent.left)
		l.append(parent.info)
		inOrder(parent.right)
	
def successor(x):
	if x in l:
		s=len(l)-1
		i=l.index(x)
		if s==i:
			return x
		else:
			m=l[i+1]
			return m
	else:
		return print("Error")

def predecessor(x):
	if x in l:
	
		i=l.index(x)
		if i==0:
			return print(x,"is the smallest element")
		else:
			m=l[i-1]
			return print(m,"is the Predecessor of",x)
	else:
		return print("Error")







	




	 
		


def main():
	tree=BST()
	while True:
		if tree.root:
			inOrder(tree.root)
		t=int(input("\nEnter \n1 to insert\n2 to print in preOrder\n3 to Search\n4 to Find minimum\n5 to print maximum\n6 to find Succesor of a number\n7 to find Predecessor of a number\n8 to delete\n9 to exit\n"))
		if (t==1):
			i=input("Enter numbers to be inserted\n")
			n=i.split()
			j=len(n)
			for k in range(j):
				tree.insert(int(n[k]))
		elif t==3:
			i=int(input("Enter numbers to be Search\n"))
			print(Search(tree.root,i))

		elif t==4:
			print("Minimun is ",minimum(tree.root))

		elif t==2:
			preOrder(tree.root)
		elif t==5:
			print("Maximum is ",maximum(tree.root))

		elif t==6:
			i=int(input("Enter a number\n"))
			print("Succesor of",i,"is",successor(i))

		elif t==7:
			i=int(input("Enter a number\n"))
			predecessor(i)
		elif t==8:
			i=int(input("Enter a number\n"))
			delete(tree.root,i)
		elif t==9:
			break
		else:
			print("Wrong input")


		

	
if __name__=='__main__':
	main()

