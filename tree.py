
# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.child = []
#         self.parent = None


#     def get_level(self):
#         level = 0
#         p = self.parent

#         while p:
#             level += 1
#             p = p.parent
        
#         return level

#     def add_child(self,child):
#         child.parent = self
#         self.child.append(child)


#     def display_tree(self):
#         spaces = " " * self.get_level() * 3
#         print(spaces,self.data)
#         if self.child:
#             for child in self.child:
#                 child.display_tree()

        

# def build_product_tree():
#     root = TreeNode("Electronics")

#     Laptop = TreeNode("Laptop")
#     Laptop.add_child(TreeNode("OMEN"))
#     Laptop.add_child(TreeNode("ACER"))

#     Mobile = TreeNode("Mobile")
#     Mobile.add_child(TreeNode("Samsung"))
#     Mobile.add_child(TreeNode("Oppo"))

#     TV = TreeNode("Television")
#     TV.add_child(TreeNode("32 Inch"))
#     TV.add_child(TreeNode("55 Inch"))


#     root.add_child(Laptop)
#     root.add_child(Mobile)
#     root.add_child(TV)



#     root.display_tree()




# if __name__ == '__main__':
#     build_product_tree()

# from typing import List

# class BinarySearchTreeNode:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_child(self,child):
#         if child == self.data:
#             return 

#         if child < self.data:
#             if self.left:
#                 self.left.add_child(child)
#             else:
#                 self.left = BinarySearchTreeNode(child)
#         else:
#             if self.right:
#                 self.right.add_child(child)
#             else:
#                 self.right = BinarySearchTreeNode(child)

#     def in_order_traversal(self):
#         elements = []

#         if self.left:
#             elements += self.left.in_order_traversal()

#         elements.append(self.data)

#         if self.right:
#             elements += self.right.in_order_traversal()

#         return elements
    
#     def search(self,val):
#         if val == self.data:
#             return True
#         elif val < self.data:
#             if self.left:
#                 return self.left.search(val)
#             else:
#                 return False
#         elif val > self.data:
#             if self.right:
#                 return self.right.search(val)
#             else:
#                 return False
            
            
    
# def build_trees(elements:List[int]):
#     root = BinarySearchTreeNode(elements[0])

#     for i in range(1,len(elements)):
#         root.add_child(elements[i])

#     return root

# if __name__ == "__main__":

#     numbers = [17,4,1,20,9,23,18,34]
#     number_tree = build_trees(numbers)
#     #print(number_tree.in_order_traversal())
#     ans = number_tree.search(99)
#     print(ans)


# class TreeNode:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.child = []
#         self.parent = None
    
#     def add_child(self,child) -> None:
#         child.parent = self
#         self.child.append(child)

#     def get_level(self):
#         level = 0

#         p = self.parent

#         while p:
#             level += 1
#             p = p.parent

#         return level


#     def print_tree(self):
#         spaces = " " * self.get_level()
#         print(spaces , self.data)

#         if self.child:
#             for child in self.child:
#                 child.print_tree()

    
# def build_tree():
#     root = TreeNode('Electronics')

#     TV = TreeNode('TV')
#     TV.add_child(TreeNode("SAMSUNG"))
#     TV.add_child(TreeNode("LG"))
    
#     Mobile = TreeNode('Mobile')
#     Mobile.add_child(TreeNode("OPPO"))
#     Mobile.add_child(TreeNode("VIVO"))
    
#     LAPTOP = TreeNode('LAPTOP')
#     LAPTOP.add_child(TreeNode("OMEN"))
#     LAPTOP.add_child(TreeNode("CHOMEN"))
    
#     root.add_child(TV)
#     root.add_child(Mobile)
#     root.add_child(LAPTOP)

#     return root
#     #root.print_tree()


# if __name__ == '__main__':
#     ans = build_tree()
#     ans.print_tree()

from typing import List

class BinarySearchTree:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data)->None:
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_trasversal(self)->List:
        elements = []

        if self.left:
            elements += self.left.in_order_trasversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_trasversal()

        return elements
    
    def pre_order(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order()
        if self.right:
            elements += self.right.pre_order()

        return elements
    
    def post_order(self):

        elements = []



        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()

        elements.append(self.data)

        return elements

    def search_method(self,val)-> bool:

        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search_method(val)
                return
            else:
                return False
            
        else:
            if self.right:
                return self.right.search_method(val)
                return
            else:
                return False


    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
        

    def delete_node(self,val):
        if val < self.data:
            if self.left:
                self.left.delete_node(val)
            
        elif val > self.data:
            self.right.delete_node(val)

        else:
            if self.left is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        

        return self
            
    
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    lst = [17,4,1,20,9,23,18,34]

    tree = build_tree(lst)
    
    ans = tree.in_order_trasversal()
    print(ans)
    
    # ans  = tree.post_order()
    # print(ans)
    # search_ans = tree.search_method(23999)
    # print(search_ans)

    tree.delete_node(20)

    res = tree.search_method(20)
    print(res)

    ans = tree.in_order_trasversal()
    print(ans)

# from typing import List

# class BinarySearchTreeNode:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_child(self,child):
#         if child == self.data:
#             return 

#         if child < self.data:
#             if self.left:
#                 self.left.add_child(child)
#             else:
#                 self.left = BinarySearchTreeNode(child)
#         else:
#             if self.right:
#                 self.right.add_child(child)
#             else:
#                 self.right = BinarySearchTreeNode(child)

#     def in_order_traversal(self):
#         elements = []

#         if self.left:
#             elements += self.left.in_order_traversal()

#         elements.append(self.data)

#         if self.right:
#             elements += self.right.in_order_traversal()

#         return elements
    
#     def search(self,val):
#         if val == self.data:
#             return True
#         elif val < self.data:
#             if self.left:
#                 return self.left.search(val)
#             else:
#                 return False
#         elif val > self.data:
#             if self.right:
#                 return self.right.search(val)
#             else:
#                 return False
            
            
    
# def build_trees(elements:List[int]):
#     root = BinarySearchTreeNode(elements[0])

#     for i in range(1,len(elements)):
#         root.add_child(elements[i])

#     return root

# if __name__ == "__main__":

#     numbers = [17,4,1,20,9,23,18,34]
#     number_tree = build_trees(numbers)
#     #print(number_tree.in_order_traversal())
#     ans = number_tree.search(99)
#     print(ans)