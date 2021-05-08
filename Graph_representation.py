class Node:
	def __init__(self,val=None):
		self.val=val
		self.next=None


def insert(T,t1,t2):
	if T[t1.val] is None:
		T[t1.val]=t2
	else:
		current=T[t1.val]
		prev=current
		while current is not None:
			prev=current
			current=current.next
		prev.next=t2

def printList(T,n):
	for i in range(len(T)):
		print("Vertex ",i ,":",end=" ")
		current=T[i]
		while current is not None:
			print(current.val,end=" ")
			current=current.next
		print()

				
def main():
	n=int(input("Enter the number of vertices: "))
	T=[None]*n
	p=int(input("Enter no. of Edges: "))
	m=p
	A=[None]*n
	B=[]
	for i in range(n):
		A[i]=[0]*n

	i=0
	while i<p:
		l=input()
		l=l.split()
		t1=Node(int(l[0]))
		t2=Node(int(l[1]))
		insert(T,t1,t2)
		insert(T,t2,t1)
		A[int(l[0])][int(l[1])]=1
		A[int(l[1])][int(l[0])]=1
		i=i+1
	print("The adjacency list is:")
	printList(T,n)
	print("The adjacency matrix is")
	for j in range(n):
		for k in range(n):
			print(A[j][k],end=" ")
		print()

if __name__=='__main__':
	main()
