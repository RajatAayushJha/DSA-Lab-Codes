import random

def main():
	print("Enter the number of men : ")
	n=int(input())
	n=int(n)
	
	men=[None for i in range(0,n)]
	women=[None for i in range(0,n)]

	print("Enter the list of all men :")
	for i in range(0,n):
		men[i]=input();

	print("Enter the list of all women :")
	for i in range(0,n):
		women[i]=input();

	men_pref=[[None for i in range(0,n)] for j in range(0,n)]
	women_pref=[[None for  i in range(0,n)] for j in range(0,n)]

	print("Enter men's preference list : ")
	for i in range(0,n):
		for  j in range(0,n):
			w=input()
			for k in range(0,n):
				if (w==women[k]):
					men_pref[i][j]=k

	
	print("Enter women's preference list : ")
	for i in range(0,n):
		for  j in range(0,n):
			m=input()
			for k in range(0,n):
				if (m==men[k]):
					women_pref[i][j]=k

	w_pref=[[-1 for i in range(0,n)] for j in range(0,n)]

	for i in range(0,n):
		t=0
		for j in range(0,n):

			k=women_pref[i][j]
			w_pref[i][k]=t
			t=t+1


	
   
	men_engagement=[None for i in range(0,n)]
	women_engagement=[-1 for i in range(0,n)]
	i=0
	j=0
	women_free=[[-1 for i in range(0,n)]]

	while((men_engagement[i]==None)):
		w=men_pref[i][j]
		print("hey")
		if (women_free[w]==-1):
			print("bye")
			men_engagement[i]=w
			women_engagement[w]=i
			women_free[w]=i
			i=i+1
			print(w,i,j)
		else:
			if (w_pref[w][i]>women_engagement[w]):
				men_engagement[i]=w
				women_engagement[w]=i
				men_engagement[women_engagement[w]]=None
				i=women_engagement[w]
				print(w,i,j)
			else:
				j=j+1
				print(w,i,j)

	print(men_engagement)




if __name__=="__main__":
	main()
