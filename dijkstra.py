import heapq
global time

class Node:
	def __init__(self):
		self.value=None
		self.next=None

def insert(t,t1,t2):
	if t[t1] is None:
		t[t1]=Node()
		t[t1].value=t2
	else:
		current=t[t1]
		prev=None
		while(current is not None):
			prev=current
			current=current.next
		prev.next=Node()
		prev.next.value=t2

def print_list(t,v):
	for i in range(0,v):
		current=t[i]
		print("Vertex ",i," : ",end=' ')
		while(current is not None):
			print(current.value," ",end=' ')
			current=current.next
		print()

class Vertex:
	def __init__(self):
		self.color=-1
		self.parent=None
		self.d=0
		self.f=0
		self.distance=1000

def dikstral(v,e,s,edge_set):
	r=[Vertex() for i in range(0,v)]
	r[s].distance=0
	z=[[0 for i in range(0,v)] for i in range(0,v)]
	print(z)
	print("Input the path weights : ")
	for i in range(0,e):
		a=input()
		b=a.split(" ")
		z[int(b[0])][int(b[1])]=int(b[2])
		z[int(b[1])][int(b[0])]=int(b[2])
	print(z)
	h=[]
	for i in range(0,v):
		heapq.heappush(h,i)
		heapq.heapify(h)
	while(len(h)!=0):
		w=h[0]
		heapq.heappop(h)
		current=edge_set[w]
		while current!=None:
			if(r[current.value].distance>r[w].distance+z[w][current.value]):
				r[current.value].distance=r[w].distance+z[w][current.value]
				heapq.heapify(h)
				r[current.value].parent=w
			
			print(w," : ",z[w][current.value])
			current=current.next


def main():
	v=int(input("Enter the number of vertices : "))
	e=int(input("Enter the number of edges : "))
	edge_set=[None]*v
	print("Enter the pair of adjacent vertices : ")
	for i in range(0,e):
		a=input()
		b=a.split(" ")
		insert(edge_set,int(b[0]),int(b[1]))
		insert(edge_set, int(b[1]),int(b[0]))
	print_list(edge_set,v)
	s=int(input("Enter the source : "))
	dikstral(v,e,s,edge_set)




if __name__=='__main__':
	main()
