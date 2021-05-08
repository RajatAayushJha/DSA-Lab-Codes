class Stack:
 def __init__(self):
   self.top=-1
   self.l=[]
   
 
 def push(self,x):
   self.top=self.top+1
   if len(self.l)==self.top:
     self.l.append(x)
   self.l[self.top]=x
   
 def pop(self):
  if(self.top==-1):
    return(False)
  else:
   self.top=self.top-1
   return self.l[self.top+1]

 def isEmpty(self):
  if (self.top==-1):
    return True
  else :
    return False

