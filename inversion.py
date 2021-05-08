
'''
for i in range(0,len(a)):
	for j in range(i+1,len(a)):
		if (a[i]>a[j]):
			count+=1
print(count)
'''
def MergeSort(a,count):
	if (len(a)>1):
		mid=int(len(a)/2)
		l=a[:mid]
		r=a[mid:]
		MergeSort(a[:mid],count)
		MergeSort(a[mid:],count)

		i=j=k=0

		while(i<len(l) and j<len(r)):
			if(l[i]<r[j]):
				a[k]=l[i]
				k+=1
				i+=1
			elif(l[i]>=r[j]):
				a[k]=r[j]
				k+=1
				j+=1
				count+=len(l)-i

		while(i!=len(l)):
			a[k]=l[i]
			k+=1
			i+=1
		while(j!=len(r)):
			a[k]=l[j]
			k+=1
			j+=1

a=[4,10,8,2,1]
count=0
MergeSort(a,count)
print(count)
