from Stack import Stack
def topostfix(expr):
 a=expr.split()
 s=Stack()
 r=Stack()
 l=len(a)
 symb=0
 while (symb != l):
   if (a[symb]=='*' or a[symb]=='/'):
    t=a.pop(symb)
    a.insert(symb+1,t)
    symb=symb+1
   symb=symb+1
 
 for symb in a:
   if (symb=='+' or symb=='-'):
    s.push(symb)
    i=a.index(symb)
    a.pop(i)
  
  
 for i in a:
   if(s.top==-1):
    pass
   else:
    a.append(s.pop())
 print(''.join(a))

expr=input("Enter a infix expression")
topostfix(expr)
