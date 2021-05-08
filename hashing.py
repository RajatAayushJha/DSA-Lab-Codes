class ListNode:
	def __init__(self,value=None,next=None,key=None):
		self.value=value
		self.next=next
		self.key=key

T=[None for i in range(30)]
def Com(s):
	l=len(s)
	i=0
	sum=0
	while i!=l:
		sum=sum+ord(s[i])
		i=i+1
	return sum
def insert(sum,val):
	k=sum%30
	temp=ListNode()
	temp.value=val
	temp.next=None
	temp.key=sum
	if T[k]==None:
		T[k]=temp
		return
	art=T[k]
	while art.next!=None:
		art=art.next
	art.next=temp


def search(val):
	sum=Com(val)
	k=sum%30
	temp=T[k]
	i=0
	if T[k]==None:
		return print("Search unsuccessfull\n")
	else:
		while temp.next!=None:

			if temp.value==val:
				return print("Search Successfull ,found at ",k,"th haskkey and at ",i,"th index of the list\n")
			temp=temp.next
			i=i+1
		if temp.value==val:
			return print("Search Successfull found at ",k,"th hashkey and at ",i,"th index of list\n")
		return print("Search unsuccessfull\n")
def key(T):
	i=0
	while i!=30:
		if T[i]!=None:
			temp=T[i]
			while temp.next!=None:
				print(temp.value)
				temp=temp.next
			print(temp.value)
		i=i+1
	return

def main():
	while True:
		ch=int(input("\nEnter\n1 for inserting\n2 for searching\n3 for printing key values\n4 for exit\n"))
		if ch==1:
			inp=input("Enter the input\n")
			sum=Com(inp)
			insert(sum,inp)
		elif ch==2:
			s=input("Enter the value to search\n")
			search(s)
		elif ch==3:
			key(T)
		elif ch==4:
			break
		else:
			print("Invalid choice\n")
	print()

	
if __name__=='__main__':
	main()



