class Node:
    def __init__(self,data=None,next=None) :
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=Node(data,None)


    
    def printlist(self):
        if self.head is None:
            print("List is Empty")
            return
        curr=self.head
        
        while(curr):
            print(curr.data,end='-->')
            curr=curr.next
        print(None)
    
    def reverse(self):
        if self.head==None:
            return None
        prev=None
        curr=self.head
        after=curr.next
        while curr:
            curr.next=prev
            prev=curr
            curr=after
            if after:
                after=after.next

        self.head=prev
def isEqual(list1,list2):
    n1=list1
    n2=list2
    while(n1!=None and n2!=None):
        if n1.data!=n2.data:
            return False
        n1=n1.next
        n2=n2.next
    if n1!=None or n1!=None:
        return False
    return True


        
          
if __name__=='__main__':
    
    l1=LinkedList()
    l2=LinkedList()
    l3=LinkedList()
    n=int(input())
    list1=list(map(int,input().strip().split())) #taking input in one line 
    for i in list1:
        l1.insertAtEnd(i)
    for i in list1:
        l3.insertAtEnd(i) #making a copy of the original linked list l1 because it is going to be reversed later

    l1.reverse()
    curr=l1.head #Storing the reversed linked list in in a new list l2
    while(curr):
        l2.insertAtEnd(curr.data)
        curr=curr.next
   

    
    print(isEqual(l2.head,l3.head))#Uses Comparison function outside the class 

    
   


