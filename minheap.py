class minheap:
	def __init__(self,tree=None):
		self.last=0
		if tree==None:
			self.tree=[None]
		else:
			self.tree=[None]+tree
			'''BUILD HEAP'''
			self.last=len(self.tree)
			y=self.parent(self.last)
			while y>=1:
				self.heapify(y)
				y=y-1

	def left(self,r):
		l= len(self.tree)
		if 2*r > l-1 or 2*r>self.last:
			return None
		return 2*r

	def right(self,r):
		l= len(self.tree)
		if 2*r+1 > l-1 or 2*r+1 > self.last:
			return None
		return 2*r+1

	def parent(self,r):
		l= len(self.tree)
		if r > l-1:
			return "element does not exist"
		return r//2

	def insert(self,x):
		self.last+=1
		if len(self.tree)==self.last :
			self.tree.append(x)
		else:
			self.tree[self.last]=x
		z=self.last
		y=self.parent(z)
		while self.tree[y]!=None and x[1] < self.tree[y][1]:
			c=self.tree[z]
			self.tree[z]=self.tree[y]
			self.tree[y]=c
			z=y
			y=self.parent(y)
		return self.tree
	
	def heapify(self,r):
		y=r
		t1=self.right(y)!=None and self.tree[self.right(y)][1]<self.tree[y][1]
		t2=self.left(y)!=None and self.tree[self.left(y)][1]<self.tree[y][1]
		while t1 or t2:
			if self.right(y)!=None and self.tree[self.right(y)][1]<self.tree[y][1]:
				if self.left(y)==None or self.tree[self.right(y)][1]<self.tree[self.left(y)][1]:
					c=self.tree[y]
					self.tree[y]=self.tree[self.right(y)]
					self.tree[self.right(y)]=c
					y=self.right(y)
			if self.left(y)!=None and self.tree[self.left(y)][1]<self.tree[y][1]:
				if self.right(y)==None or self.tree[self.left(y)][1]<self.tree[self.right(y)][1]:
					c=self.tree[y]
					self.tree[y]=self.tree[self.left(y)]
					self.tree[self.left(y)]=c
					y=self.left(y)
			t1=self.right(y)!=None and self.tree[self.right(y)][1]<self.tree[y][1]
			t2=self.left(y)!=None and self.tree[self.left(y)][1]<self.tree[y][1]
		return self.tree

	def minimum(self):
		if len(self.tree)==1:
			return "heap is empty"
		return self.tree[1]

	def extractmin(self):
		if self.last==0:
			return "heap is empty"
		c=self.tree[1]
		self.tree[1]=self.tree[self.last]
		self.tree[self.last]=c
		self.last-=1
		self.heapify(1)
		return c

	def isEmpty(self):
		if self.last==0:
			return True
		return False

	def heap(self):
		return self.tree[1:]

	def updatepriority(self,v,x):
		for i in range(1,len(self.tree)):
			if self.tree[i][0]==v:
				break
		self.tree[i]=(self.tree[i][0],x)
		for j in range(i,0,-1):
			self.heapify(j)
		return self.tree


def main():
	a=minheap([(12,1),(123,3),(1,5)])
	print(a.heap(),"  ",a.minimum(),a.updatepriority(123,0))

if __name__=='__main__':
	main()
