class heap:
	def __init__(self):
		self.parent=None
		self.left=None
		self.right=None
		self.l=[]
	def heapify(self,i):
		if ((2*i+1) <= (len(self.l)-1) and self.l[2*i+1]>self.l[i]):
			largest=2*i+1
			print("hey")
		else:
			largest=i
			if ((2*i+2) <=(len(self.l)-1)and self.l[2*i+2]>self.l[i]):
				largest=2*i+2
				print("bye")

		if ( largest != (i)):
			temp=self.l[i]
			self.l[i]=self.l[largest]
			self.l[largest]=temp

			self.heapify(largest)
		

	def maximum(self):
		return self.l[0]

	def extract_max(self):
		t=self.l[0]
		self.l[0]=self.l[len(self.l)-1]
		max=len(self.l)-1
		del[self.l[max]]
		print(len(self.l))
		self.heapify(0)
		return t

	def insert(self,x):
		self.l.append(x)
		i=len(self.l)-1
		self.parent=int(((i+1)/2) -1 )
		while (i>=0 and self.l[self.parent]<self.l[i]):
			temp=self.l[self.parent]
			self.l[self.parent]=self.l[i]
			self.l[i]=temp
			i=self.parent
			self.parent=int(((i+1)/2)-1)

	def build_heap(self):
		for i in range(int((len(self.l))/2),-1,-1):
			self.heapify(i)
		


		

def main():
	h=heap()
	h.l=[4,16,10,14,7,9,3,2,8,1]
	h.build_heap()
	print(h.l)


if __name__=='__main__':
	main()
