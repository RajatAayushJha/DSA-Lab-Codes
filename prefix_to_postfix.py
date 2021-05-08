from Stack import Stack

def toPostfix(expr):
 a=expr.split()
 print(a)
 l=len(a)
 symb=0
 while(symb != l):
  if (a[symb]=='*' or a[symb]=='/'):
     t=a.pop(symb)
     a.insert(symb+2,t)
     symb=symb+2
  symb=symb+1
     
 print(a)
 
 for symb in a:
  if (a[0]=='+' or a[0]=='-'):
    s(a)
 print(''.join(a))

def s(a):
 for symb in a:
   if (symb=='-' or symb=='+'):
     i=a.index(symb)
     a.pop(i)
     a.append(symb)
 print(a)

expr=input("Enter an prefix expression")
toPostfix(expr)
