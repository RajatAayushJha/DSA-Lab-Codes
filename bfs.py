class Vertex:
	def __init__(self,dist=(-1),col=(-1),par=None):
		self.dist=dist
		self.col=col
		self.par=par

class Queue:
	def __init__(self):
		self.T=[]
	def enqueue(self,x):
		self.T.append(x)

	def dequeue(self):
		return self.T.pop(0)
	def Empty(self):
		if len(self.T)==0:
			return False
		return True

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
	temp=Vertex()
	i=0
	U=[None]*n
	while i<n:
		U[i]=Vertex()
		i=i+1
	p=int(input("Enter no. of Edges: "))
	n=p
	m=p
	A=[None]*n
	B=[]
	Q=Queue()
	for i in range(p):
		A[i]=[0]*p
	i=0
	print("Enter the edges : ")
	while i<p:
		l=input()
		l=l.split()
		t1=Node(int(l[0]))
		t2=Node(int(l[1]))
		insert(T,t1,t2)
		insert(T,t2,t1)
		i=i+1
	ch=int(input("Enter a source Vertex S : "))
	Q.enqueue(ch)
	U[ch].dist=0
	print("V    D")
	while Q.Empty():
		t=Q.dequeue()
		current=T[t]
		while current is not None:
			if U[current.val].col==-1:
				U[current.val].col=0
				U[current.val].par=t
				U[current.val].dist=U[t].dist+1
				Q.enqueue(current.val)
				current=current.next
			else:
				current=current.next
		U[t].col=1
		print(t,"  ",U[t].dist)




	

	
if __name__=='__main__':
	main()
