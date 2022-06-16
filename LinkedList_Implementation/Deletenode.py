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
    
    def deleteNode(self,key):
        temp = self.head
        if(temp is not None):
            if temp.data == key:
                self.head = temp.next
                temp = None
                return 
        while