from mystack import Stack

def eval_postfix(t):
    """Evaluates the postfix expression 's'."""
    s=Stack()
    a=t.split()
    for symb in a:
    	if not (symb=='+' or symb=='-' or symb=='/' or symb=='*') :
    		s.push(symb)
    	else:
    		c=s.pop()
    		b=s.pop()
    		if symb=='+':
    			s.push(float(c)+float(b))
    		if symb=='-':
    			s.push(float(c)-float(b))
    		if symb=='/':
    			s.push(float(c)/float(b))
    		if symb=='*':
    			s.push(float(c)*float(b))

    return s.l[s.top]

    
def main():
	expr = input('Enter the postfix expression: ')
	print('The value of the expression is',eval_postfix(expr))

if __name__ == '__main__':
    main()
