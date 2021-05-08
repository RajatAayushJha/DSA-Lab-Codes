class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
            
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        temp=ListNode()
        temp.value=x
        temp.next=pos.next
        pos.next=temp

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        if(pos.next!=None):
          pos.next=pos.next.next
        else:
          print('Already at the tail of the list')

    def print(self):
        """ Print all the elements of a list in a row."""
        l=[]
        temp=self.head.next
        while(temp!=None):
           l.append(temp.value)
           temp=temp.next
        return l

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        c=self.head
        k=0
        for j in range(1,i-1):
           if ( c.next!=None):
              c=c.next
        temp=self.head                
        temp.next=c.next
        temp=c.next     
        self.insert(x,c)

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=ListNode()
        while (temp.next!=None):
            if(temp.value==x):
                return temp
            else :    
                temp=temp.next
            

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        l=0
        temp=self.head
        while (temp.next!=None):
            l=l+1
            temp=temp.next
        return l

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if (self.head.next==None):
            return "True"
        else :
            return "False"   


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ',L.print())
    L.insert(12,L.head.next)
    print('List is: ',L.print())
    L.insert(2,L.head)
    print('List is: ',L.print())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',L.print())
    L.delete(L.head.next)
    print('List is: ',L.print())
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ',L.print())
if __name__ == '__main__':
    main()
