class Node:
	def __init__(self):
		self.value=None
		self.next=None

def insert(t,t1,t2,t3):
	if t[t1] is None:
		t[t1]=Node()
		t[t1].value=[t2,t3]
	else:
		current=t[t1]
		prev=None
		while(current is not None):
			prev=current
			current=current.next
		prev.next=Node()
		prev.next.value=[t2,t3]

def print_list(t,v):
	for i in range(0,v):
		current=t[i]
		print("Vertex ",i," : ",end=' ')
		while(current is not None):
			print(current.value," ",end=' ')
			current=current.next
		print()

def relax (edge_set,v,s):
	T=[[float("inf") for i in range(0,v)] for i in range(0,v)]
	T[s]=[0 for i in range(0,v)]
	edge_set=[[[1,10],[7,8]],[[5,2]],[[3,1],[1,1]],[[4,3]],[[5,-1]],[[2,-2]],[[5,-1],[1,-4]],[[6,1]]]
	for k in range(0,v):
		for j in range(0,v):
			for i in range(len(edge_set[j]):
				if (T[edge_set[j][i][0]][k]>T[i][k-1]+edge_set[j][i][1]):
					T[edge_set[j][i][0]][k]=T[i][k-1]+edge_set[j][i][1]

	print(T)








def main():
	v=int(input("Enter the number of vertices : "))
	e=int(input("Enter the number of edges : "))
	edge_set=[None]*v
	'''print("Enter the pair of adjacent vertices : ")
	for i in range(0,e):
		a=input()
		b=a.split(" ")
		insert(edge_set,int(b[0]),int(b[1]),int(b[2]))
	print_list(edge_set,v)'''
	s=int(input("Enter the source : "))
	relax(edge_set,v,s)




if __name__=='__main__':
	main()		
