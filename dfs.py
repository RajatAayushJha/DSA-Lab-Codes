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

def dfs(v,e,edge_set,s):
	r=[Vertex() for i in range(0,v)]
	global time
	time=0
	for i in range(0,v):
		if r[i].color==-1:
			visit(i,r,edge_set,v)

def visit(i,r,edge_set,v):
	global time
	time+=1
	r[i].d=time
	r[i].color=0
	current=edge_set[i]
	while(current is not None):
		if r[current.value].color==-1:
			visit(current.value,r,edge_set,v)
		current=current.next
	r[i].color=1
	time+=1
	r[i].f=time
	print(i,":",r[i].d,r[i].f)








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
	dfs(v,e,edge_set,s)




if __name__=='__main__':
	main()
