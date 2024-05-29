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

