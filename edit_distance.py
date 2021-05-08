s1=input("Enter first string : ")
s1=" "+s1
s2=input("Enter second string : ")
s2=" "+s2
m=len(s2)
n=len(s1)
print(m,n)
T=[[None for j in range(0,m)] for i in range(0,n)]
x=0
y=0
z=0

def difference(i,j):
	if(s1[i] is not s2[j]):
		return 1
	else:
		return 0

def E(i,j):
	if(T[i][j] is not None):
		return T[i][j]
	elif (i is 0):
		T[i][j]=j
		return T[i][j]
	elif (j is 0):
		T[i][j]=i
		return T[i][j]
	else:
		x==(difference(i,j)+E(i-1,j-1))
		y=(1+E(i-1,j))
		z=(1+E(i,j-1))
		if ((x<y) and (x<z)):
			T[i][j]=x
		elif((y<x) and (y<z)):
			T[i][j]=y
		else:
			T[i][j]=z
		return (T[i][j])

print(E(len(s1)-1,len(s2)-1))
