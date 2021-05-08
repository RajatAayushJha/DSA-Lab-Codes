def peak(a,n,start,mid,end):
	if(a[mid]>a[mid+1] and a[mid]>a[mid-1]):
		print( a[mid])
	elif(a[mid]<a[mid+1]):
		start=mid-1
		mid=int((start+end)/2)
		peak(a,end-start+1,start,mid,end)
	elif(a[mid]<a[mid-1]):
		end=mid
		mid=int((start+end)/2)
		peak(a,end-start+1,start,mid,end)

a=[2,4,6,8,7,5,3]
peak(a,7,0,3,6)
b=[10,12,8,4,-3,-15]
peak(b,6,0,3,5)
