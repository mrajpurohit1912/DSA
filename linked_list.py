# class Node:
#     def __init__(self,data=None,next = None) -> None:
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     # def insert_at_begining(self,data):
#     #     if self.head is None:
#     #         self.head = Node(data)
        
#     #     h = self.head
#     #     while self.head:
#     #         self.head = self.head.next
#     def insert_at_beg(self,data):
#         new_node = Node(data,self.head)
#         self.head = new_node

#     def display_linked_list(self):
#         if self.head is None:
#             return
        
#         while self.head:
#             print(self.head.data)
#             self.head = self.head.next

#     def insert_at_end(self,data):
#         if self.head is None:
#             new_node = Node(data,None)
#             return
#         # while self.head:
#         #     self.head = self.head.next 
#         #     if self.head == None:
#         #         new_node = Node(data)
#         #         self.head = new_node

#         itr = self.head
#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data,None)

#     def insert_values(self,data_list):
#         self.head = None

#         for data in data_list:
#             self.insert_at_end(data)



# if __name__ == '__main__':
#     l = LinkedList()
#     # l.insert_at_beg(3)
#     # l.insert_at_beg(2)
#     # l.insert_at_beg(1)
#     # l.insert_at_beg(4)
#     #print(l.display_linked_list())
#     # l.insert_at_end(99)
#     l.insert_values(["APPLE","BANANA","GRAPES"])
#     l.display_linked_list()

################################################################################

# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def insert_at_beg(self,val):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#             return
#         #temp = self.head
#         else:
#             # self.head = new_node
#             # self.head.next = temp
#             new_node.next = self.head
#             self.head = new_node  


#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         else:
#             current_node = self.head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node

        

#     def display(self):
#         # while self.head:
#         #     print(self.head)
#         #     self.head = self.head.next
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next


# l = LinkedList()

# l.insert_at_beg(3)
# l.insert_at_beg(2)
# l.insert_at_beg(1)
# l.insert_at_end(4``)

# l.display()

########################################################################################################
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next= None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def insert_at_beg(self,val) -> None:
#         new_node = Node(val)

#         if not self.head:
#             self.head = new_node
#             return
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def insert_at_end(self,val):
#         new_node = Node(val)

#         if not self.head:
#             self.head = new_node
#             return
        
#         current_node = self.head
#         while(current_node.next):
#             current_node = current_node.next
#         current_node.next = new_node

#     def insert_at_index(self,val,index):
        
#         new_node = Node(val)

#         position = 0
#         current_node = self.head
#         if position == index:
#             self.insert_at_beg(val)
#         else:
#             while(current_node != None and position+1 != index):
#                 position = position + 1
#                 current_node = current_node.next

#                 if current_node != None:
#                     new_node.next = current_node.next
#                     current_node = new_node
#                 else:
#                     print("index is not present")


#     def update_node(self,data,index):
#         current_node = self.head
#         position = 0

#         if position == index:
#             self.head.data = data
#         else:
#             while(position != index and current_node != None):
#                 position = position +1
#                 current_node = current_node.next
#             if current_node != None:
#                 current_node.data = data
#             else:
#                 print("Index is not present")
#     def updateNode(self, val, index):
#         current_node = self.head
#         position = 0
#         if position == index:
#             current_node.data = val
#         else:
#             while(current_node != None and position != index):
#                 position = position+1
#                 current_node = current_node.next

#             if current_node != None:
#                 current_node.data = val
#             else:
#                 print("Index not present")

#     def display(self):
#         current_node = self.head
#         while(current_node):
#             print(current_node.data)
#             current_node = current_node.next


#     def remove_first_node(self):
#         if self.head == None:
#             return
        
#         self.head == self.head.next

#     def remove_last_node(self):
#         if not self.head:
#             return 
#         current_node = self.head
#         while (current_node != None and current_node.next.next != None):
#             current_node = current_node.next

#         current_node.next = None
    
#     def remove_node_at_index(self,index):

#         if not self.head:
#             return
        
#         position = 0
#         current_node = self.head

#         if position == index:
#             self.remove_first_node()

#         else:
#             while(current_node != None and position+1 != index):
#                 current_node = current_node.next
#                 position = position +1
#             if current_node != None:
#                 current_node.next = current_node.next.next
#             else:
#                 print("Index is not present")
        


# l = LinkedList()

# l.insert_at_beg(3)
# l.insert_at_beg(2)
# l.insert_at_beg(1)

# l.insert_at_end(4)
# l.insert_at_end(5)

# #l.remove_node_at_index(1)
# #l.remove_first_node()
# l.remove_first_node()
# l.remove_first_node()

# #l.insert_at_index(99,3)
# #l.update_node(2,99)
# l.updateNode(2,99)

# l.display()
#######################################################################################
# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
    
#     def insert_at_beg(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
        
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self,data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#             return

#         current_node = self.head
#         while(current_node.next):
#             current_node = current_node.next
#         current_node.next = new_node

#     # def insert_at_index(self,data,index):
#     #     new_node = Node(data)
#     #     position = 0

#     #     if index == 0:
#     #         #self.head = new_node
#     #         self.insert_at_beg(data)
#     #         return
        
#     #     current_node = self.head

#     #     while(current_node != None and position+1 != index):
#     #         position = position+1
#     #         current_node = current_node.next 

#     #     if current_node != None:
#     #         # current_node.next.next = current_node.next
#     #         # current_node.next = new_node
#     #         new_node.next = current_node.next
#     #         current_node.next = new_node
#     #     else:
#     #         print("Index Not found !")
#     def insertAtIndex(self, data, index):
#         if (index == 0):
#             self.insert_at_beg(data)
            
#         position = 0
#         current_node = self.head
#         while (current_node != None and position+1 != index):
#             position = position+1
#             current_node = current_node.next

#         if current_node != None:
#             new_node = Node(data)
#             new_node.next = current_node.next
#             current_node.next = new_node
#         else:
#             print("Index not present")


#     def display(self):
#         if not self.head:
#             return
#         current_node = self.head

#         while(current_node):
#             print(current_node.data)
#             current_node = current_node.next

 

#     def size_of_linked_list(self):
#         count = 0
#         if not self.head:
#             return count
        
#         current_node = self.head
#         while(current_node.next):
#             current_node = current_node.next
#             count += 1
#         print("Count is ",count) 

#     def update_node(self,data,index):
#         #new_node = Node(data)
#         if index == 0:
#             #new_node.next = self.head.next
#             self.head.data = data 
#             return
        
#         position = 0
#         current_node = self.head
#         while(current_node != None and position+1 != index):
#             position += 1
#             current_node = current_node.next

#         if current_node != None:
#             current_node.data = data
#         else:
#             print("Index is not present")

# l = LinkedList()
# #l.insertAtIndex(99,1)
# l.insert_at_beg(3)            
# l.insert_at_beg(2)            
# l.insert_at_beg(1)            
# l.insert_at_end(4)
# l.insert_at_end(99)
# l.insert_at_end(5)
# l.update_node(6,7)

# #l.size_of_linked_list()                               
# l.display()
        
        
class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertatbeg(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insertatend(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def size_of_list(self):
        size_pointer = 0

        if not self.head:
            return size_pointer

        current_node = self.head
        while current_node:
            size_pointer += 1
            current_node = current_node.next

    def remove_first_node(self):

        if not self.head:
            return

        self.head = self.head.next

    def remove_last_nose(self):

        if not self.head:
            return

        current_node = self.head
        while current_node.next.next != None:
            current_node  = current_node.next

        current_node.next = None        
