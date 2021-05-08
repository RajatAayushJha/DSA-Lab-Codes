class Node:
	def __init__(self,value=None,left=None,right=None,parent=None):
		self.key=value
		self.left=left
		self.right=right
		self.parent=parent

class BST:
	def __init__(self):
		self.head=Node()


def parse(s,root):
	expr=s.split()
	l=len(expr)
	i=0
	current=root
	while i<l:
		symb=expr[i]
		i=i+1
		if symb=='(':
			temp=Node()
			current.left=temp
			temp.parent=current
			current=temp

		elif symb in ['+','-','*','/']:
			current=current.parent
			current.key=symb
			temp=Node()
			current.right=temp
			temp.parent=current
			current=temp

		elif symb==')':
			current=current.parent

		else:
			current.key=symb
	return

'''def inOrder(present):
	if present:
		inOrder(present.left)
		print(present.key,end=" ")
		inOrder(present.right)'''


def printPrefix(parent):
	if parent:
		print(parent.key,end=" ")
		printPrefix(parent.left)
		printPrefix(parent.right)

def printPostfix(parent):
	if parent:
		printPostfix(parent.left)
		printPostfix(parent.right)
		print(parent.key,end=" ")

def evaluateTree(root):
	if not root:
		return 0
	if root.left is None and root.right is None: 
		return int(root.key) 
	left_res=evaluateTree(root.left)
	right_res=evaluateTree(root.right)
	if root.key=='+':
		return (left_res+right_res)
	if root.key=='-':
		return (left_res-right_res)
	if root.key=='*':
		return (left_res*right_res)
	if root.key=='/':
		return (left_res/right_res)








def main():
	tree=BST()
	s=input("Enter a valid expression: ")
	parse(s,tree.head)
	#inOrder(tree.head)
	#print("")
	print("Prefix Expression: ",end="")
	printPrefix(tree.head)
	print("")
	print("Postfix Expression: ",end="")
	printPostfix(tree.head)
	print("Result: ",evaluateTree(tree.head))


if __name__=='__main__':
	main()
