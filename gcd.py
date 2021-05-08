def gcd(a,b):
  if(a>b):	
    k=a%b
    if(k==0):
     print(b,'is the gcd')
    else:
     gcd(b,k)
  else:
    k=b%a
    if(k==0):
     print(a,'is the gcd')
    else:
     gcd(a,k)

gcd(int(input("enter first positive number\n")),int(input("Enter second positive number\n")))
