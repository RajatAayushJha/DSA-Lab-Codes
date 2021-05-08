class Node:
	def __init__(self,x):
		self.parent=None
		self.value=x

def Bottom_up_LPath(t):
	A=[None for i in range(0,len(t))]
	n=len(t)
	l=[None for i in range(0,n)]
	print(t)
	for i in range(0,n):
		A[i]=Node(t[i])
	

	T=[0 for i in range(0,n)]
	for i in range(n-1,-1,-1):
		maximum=0
		for j in range(i+1,n):
			if(t[i]<t[j]):
				if (maximum<(1+T[j])):
					maximum=1+T[j]
					A[i].parent=A[j].value
					l[i]=A[j].value

		T[i]=maximum
	
	print("Maximum is : ",max(T)+1)

	for i in range(0,n):
		if (T[i] is max(T)):
			print(A[i].value)
			j=l.index(A[i].parent)
			k=1
			while(k is not 4):
				print(A[j].parent)
				j=B.index(A[j].parent)
				
				k+=1

B=[5,2,8,6,3,6,9,7]
Bottom_up_LPath(B)
