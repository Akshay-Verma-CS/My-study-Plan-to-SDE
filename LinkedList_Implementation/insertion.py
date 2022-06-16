class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def addatstart(self,new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
    
    def addmiddle(self,prevNode,newData):
        if prevNode is None:
            return
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
    
    def addatend(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        temp =self.head
        while(temp):
            temp = temp.next
        temp.next = newNode
        
        
