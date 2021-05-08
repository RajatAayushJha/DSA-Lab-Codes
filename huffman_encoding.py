import heapq

class Node:
	def __init__(self):
		self.symbol=None
		self.frequency=None
		self.left_child=None
		self.right_child=None
		self.parent=None
	def __le__(self,other):
		return (self.frequency <other.frequency )
	def __lt__(self,other):
		return (self.frequency<other.frequency)

def  huffman(symbols,freq,n):
	leaves=[]
	pointer=[None for i in range(0,n)]
	for i in range(0,n):
		node=Node()
		node.symbol=symbols[i]
		node.frequency=freq
		leaves.append(node)
		pointer[i]=node

	heapq.heapify(leaves)
	for i in range(n-1):
		t1=heapq.heappop(leaves)
		t2=heapq.heappop(leaves)
		node=Node()
		node.frequency=(t1.frequency+t2.frequency)
		if(t1>t2):
			node.right_child=t1
			node.left_child=t2
			
		else:
			node.right_child=t2
			node.left_child=t1
		t1.parent=node
		t2.parent=node
		heapq.heappush(leaves,node)
	node=heapq.heappop(leaves)
	code=["" for i in range(0,n)]
	i=0


	for i in range(0,n):
		while(pointer[i].parent  is not None):
			if(pointer[i].parent.left_child == pointer[i]):
				code[i]+="0"
			else:
				code[i]+="1"
			pointer[i]=pointer[i].parent
		code[i]=code[i][::-1]
	print(code)





z=int(input("Enter the number of symbols used : "))
symbols=[]
freq=[]
for i in range(0,z):
	t=input().split()
	symbols.append(t[0])
	freq.append(int(t[1]))
print(symbols,freq)
huffman(symbols,freq,z)
