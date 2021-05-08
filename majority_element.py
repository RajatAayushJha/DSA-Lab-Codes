def majority_element(a):
	if (len(a)==1):
		return 1
	mid=len(a)//2
	countmajority_element(a[0:mid])
	majority_element(a[mid:])

		




a=input("Enter an array : ").split(" ")
for i in range(0,len(a)):
	a[i]=int(a[i])
