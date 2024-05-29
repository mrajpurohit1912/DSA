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
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertatbeg(self,val):
        if self.head:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node
    

    def insert_at_index(self,val,index_val):
        count = 0
        new_node = Node(val)

        if index_val == count:
            #self.insertatbeg(val)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            count += 1
            current = self.head
            while(current.next):
                if count == index_val:
                    new_node.next = current
                    current = new_node
                    return



    def display_all(self):
        # if self.head is None:
        #     print("Linked list is empth")
        # else:
        #     while self.head.next:
        #         print(self.head.data)
        #         self.head = self.head.next
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
        


if __name__ == '__main__':
    l = LinkedList()
    l.insertatbeg(3) 
    l.insertatbeg(2) 
    l.insertatbeg(1)
    l.insert_at_index(99,2)
    l.insert_at_end("Mahavir")
   
    l.display_all()
