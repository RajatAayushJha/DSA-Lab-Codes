def solve_hanoi(n,s,i,t):
	if (n>1):
		solve_hanoi(n-1,s,t,i)
		print("Move disk ",n,"from ",s,"to ",t)
		solve_hanoi(n-1,i,s,t)
	else:
		print("Move disk ",1,"from ", s,"to", t)

n=int(input("Enter number of disks : "))
solve_hanoi(n,"S","I","T")
