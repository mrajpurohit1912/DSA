# # Y shaped pattern
# class Solution:
#     def yShapedPattern(self, N):
#         for i in range(N):
#             for j in range(4):
#                 print('*', end="")
#                 N -= 1


#         # # Given integer N
#         # N = 12

#         # # Initialize s and t
#         # s = N / 2
#         # t = s

#         # # Traverse from 0 till N
#         # for i in range(0, N):

#         #     if (i > s):
#         #         for j in range(0, int(s)):
#         #             print(" ", end = "")
#         #     else:
#         #         for j in range(0, i):
#         #             print(" ", end = "")

#         #         print("*", end = "")
                
#         #         for k in range(0, (2*int(t))):
#         #             print(" ", end = "")

#         #         # Decrement t
#         #         t = t - 1

#         #     print(" *")

#         #     # This code is contributed by akashish__


# sl = Solution()
# sl.yShapedPattern(4)


# def print_y_pattern(n):
#     for i in range(n):
#         for j in range(i):
#             print(" ", end=" ")
#         for k in range(n-i):
#             print("*", end=" ")
#         print()

# print_y_pattern(4)


# n = 5
# for i in range(n,0,-1):
#     if i < n:
#         print("  " * (n - i),end="")
#         print("* " * i)
#     #print("*" * i)
#     #print(i)


# n = 5
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n - i):
#         print("*" ,end=" ")
#     print()

# n = 5 
# for i in range(n,0,-1):
#     if i < n:
#         print("  " * (n- i) ,end="")
#         print("* " * i)
#     else:
#         print("* " * i)

# n = 5

# for i in range(n,0,-1):
#     print(i)


# lst = [6,9,3,4,5]
# for i in range(len(lst),0,-1):
#     print(lst[i - 1])

# for index,i in enumerate(len(lst)):
#     print(i)

# lst = [6,9,3,4,5]

# for i in range(len(lst)):
#     for j in range(i+ 1,len(lst)):
#         temp = lst[i]
#         if lst[j] < lst[i]:
#             lst[i] = lst[j]
#             lst[j] = temp

# print(lst)

# Python3 program for Bubble Sort Algorithm Implementation
# def bubbleSort(arr):
	
# 	n = len(arr)

# 	# For loop to traverse through all 
# 	# element in an array
# 	for i in range(n):
# 		for j in range(0, n - i - 1):
# 			print(j)
# 			# # Range of the array is from 0 to n-i-1
# 			# # Swap the elements if the element found 
# 			# #is greater than the adjacent element
# 			# if arr[j] > arr[j + 1]:
# 			# 	arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
#         # Driver code

# # Example to test the above code
# arr = [ 2, 1, 10, 23 ]

# print(bubbleSort(arr))
# arr = [ 2, 1, 10, 23 ,99,54,24]

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         temp = arr[i]
#         if arr[j] < arr[i]:
#             arr[j] ,arr[i] = arr[i] ,arr[j]

# print(arr)


#Selection Sort

# data = [ 7, 2, 1, 6 ]

# for i in range(len(data)):
#     min_idx = i
#     for j in range(min_idx + 1,len(data)):
#         if data[j] < data[min_idx]:
#             min_idx = j
            
# 	data[i], data[min_idx] = data[min_idx] , data[i]
        
# print(data)


# data = [7, 2, 1, 6]

# for i in range(len(data)):
#     min_idx = i
#     for j in range(min_idx + 1, len(data)):
#         if data[j] < data[min_idx]:
#             min_idx = j
            
#     data[i], data[min_idx] = data[min_idx], data[i]
        
# # print(data)

# arr = [2, 3, 4, 10, 40]

# key = 2


# # for i in range(len(arr)):
# #     if key == arr[i]:
# #         print(arr[i], "   ", i) 

# def birnary_search(arr,key):
# 	l = 0
# 	h= len(arr) - 1

# 	while l <= h:
# 		mid  = l + (h - l) // 2
# 		if key == arr[mid]:
# 			return(arr[mid],mid)
# 		elif key < arr[mid]:
# 			h = (mid -1)
# 		elif key > arr[mid]:
# 			l  = (mid +1)
			
# print(birnary_search(arr,key))

# def print_pyramid(rows):
#     for i in range(0, rows):
#         for j in range(0, rows - i - 1):
#             print(end=" ")
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print()


# def print_pyramid(rows):
#     for i in range(rows):
#         for j in range(rows - i - 1):
#             print(end=" ")
#         for j in range(i + 1):
#             print("*",end=" ")
#         print()
# def print_pyramid(n):
#     for i in range(n,0,-1):
# 		if i < n:
# 			print("  " * (n- i) ,end="")
# 			print("* " * i)
# 		else:
# 			print("* " * i)


# n = 5
# print_pyramid(n)

# for i in range(n,0,-1):
# 		if i < n:
# 			print("  " * (n- i) ,end="")
# 			print("* " * i)
# 		else:
# 			print("* " * i)



# def print_right_triangle(rows):
#     for i in range(0, rows):
#         for j in range(0, i + 1):
#             print("*", end=" ")
#         print()


# def print_right_triangle(rows):
#     for i in range(rows):
#         print("* " *(i+1))

# rows = 5
# print_right_triangle(rows)



# def print_inverted_pyramid(rows):
#     for i in range(rows, 0, -1):
#         for j in range(0, rows - i):
#             print(end=" ")
#         for j in range(0, i):
#             print("*", end=" ")
#         print()



# def func(rows):
#     for i in range(rows,0,-1):
#         if i < rows:
#             print(" " * (rows - i))
# 		else:
#             print(" * ")

# # def func(rows):
# #     for i in range(rows, 0, -1):
# #         if i < rows:
# #             print(" " * (rows - i), end="")
# #         else:
# #             print(" ", end="")
# #         print("*" * i)

# rows = 5
# print(func(rows))


# def print_hollow_diamond(rows):
#     for i in range(rows):
#         for j in range(rows - i - 1):
#             print(" ", end="")
#         for j in range(2 * i + 1):
#             if j == 0 or j == 2 * i or i == rows - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

#     for i in range(rows - 2, -1, -1):
#         for j in range(rows - i - 1):
#             print(" ", end="")
#         for j in range(2 * i + 1):
#             if j == 0 or j == 2 * i or i == rows - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# rows = 5
# print_hollow_diamond(rows)


# from collections import deque

# # Create an empty stack
# stack = deque()

# # Push items onto the stack
# stack.append(1)
# stack.append(2)
# stack.append(3)

# # # Pop items from the stack
# print(stack.pop())  # Output: 3
# print(stack.pop())  # Output: 2
# print(stack.pop())  # Output: 1
# print(stack)
# # Check if the stack is empty
# print(len(stack) == 0)  # Output: True
#print(stack[0])



# from queue import Queue

# # Create an empty queue
# queue = Queue()

# # Enqueue items into the queue
# queue.put(1)
# queue.put(2)
# queue.put(3)

# # # Dequeue items from the queue
# print(queue.get())  # Output: 1
# print(queue.get())  # Output: 2
# print(queue.get())  # Output: 3

# # # Check if the queue is empty
# # print(queue.empty())  # Output: True

# print(list(queue.queue))


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return None

#     def is_empty(self):
#         return len(self.items) == 0


# class Stack:
    
# 	def __init__(self):
# 		self.items = []

# 	def push(self,item):
# 		self.items.append(item)

# 	def pop(self,item):
# 		if not self.is_empty():
# 			return self.items.pop()
# 		else:
# 			raise IndexError("Stack is empty")
		
# 	def is_empty(self):
# 		return len(self.items) == 0



# class qu:
    
#     def __init__(self):
#         self.itemss = []
        
# 	def push(self,item):
#         self.itemss.append(item)
            
# 	def pop(self):
#         if not is_empty():
#             return self.items.pop(0)
#         else:
#             return None
#######################################################################

# def print_all_subsets(nums):
#     def backtrack(start, subset):
#         # Add the current subset to the result
#         result.append(subset[:])
        
#         # Explore all possible subsets starting from 'start' index
#         for i in range(start, len(nums)):
#             subset.append(nums[i])
#             # Continue exploring with the next element
#             backtrack(i + 1, subset)
#             # Backtrack: Remove the last element to backtrack
#             subset.pop()
    
#     result = []
#     backtrack(0, [])
#     return result

# # Example usage
# nums = [1, 2, 3]
# print("All subsets:", print_all_subsets(nums))

    
# nums = [1,2,3]
# print('All Subsets: ',print_all_subset(nums))
#######################################################################
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# def fibonacci(n):
#     if n <= 1:
#         return n  # Base case: fibonacci(0) = 0, fibonacci(1) = 1
#     else:
#         print(fibonacci(n - 1) + fibonacci(n - 2))
#         return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)



# print(fibonacci(10))
#######################################################################
# def factorial(n):
#     if n == 0:
#         return 1  # Base case: factorial of 0 is 1
#     else:
#         return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# def my_factorial(n):
#     if n <=1:
#         return 1
#     else:
#         return n * factorial( n-1)
    

# print(factorial(0))
# print(my_factorial(0))

# def print_numbers(n):
#     if n > 10:
#         return
#     print_numbers(n+1)
#     print(n, end=' ')

# print_numbers(1)

# def func(n,sum_va):
#     if n > 0:
        
#         # func(n-1)
#         #print(n)
#         sum_va += n
#         func(n-1,sum_va)
#         return sum_va 
#     #print(sum_va) 
#     #return sum_va
# ans = func(10,0)
# print(ans)

# def printNos(n):
#     if n > 0:
#         # printNos(n - 1)
#         print(n, end=' ')
#         printNos(n - 1)

# # Driver code
# n = 10
# printNos(n)


# def recurSum(n): 
#     if n <= 1: 
#         return n 
#     return n + recurSum(n - 1) 
  
# # Driver code 
# n = 10
# print(recurSum(n)) 

# def rev_sum(n):
#     if n <= 1:
#         return n
#     return n + rev_sum(n-1)

# print(rev_sum(5))
# from typing import List
# import time

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         prev_x = x
#         rev_num = 0
#         while x != 0:
#             last_digit = x%10
#             #print(last_digit)
#             #time.sleep(3)
#             rev_num = rev_num * 10 + last_digit
#             x = x //10
#         #return rev_num

#         return rev_num == prev_x

# a = 1234
# sl = Solution()
# ans = sl.isPalindrome(a)
# print(ans)          
# # x = 1234
# # print(x)
# # print(x//10)


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         rev = str(x)[::-1]

#         if str(x) == rev:
#             return True
#         else:
#             return False    


# from typing import List


# class Solution:
#     result = ""
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         for index,char in enumerate(strs[0]):
#             for string in strs[1:]:
#                 if index >= len(string) or string[index] != char:
#                     return result
#             result += char
            
            


# strs = ["flower","flow","flight"]
# sl = Solution()
# sl.longestCommonPrefix(strs)

# class my_class:
#     class_atr = 34

#     def __init__(self,value):
#         self.value = value

#     def instance_method(self):
#         print("This is instance mthod",end=" ")
#         print(self.value)

#     @classmethod
#     def class_method(self):
#         print("This is class mehod",end=" ")
#         #print(self.value)
#         print(my_class.class_atr)

# # sl = my_class(55)
# # #sl.instance_method()
# # sl.class_method()

# my_class.instance_method()


# class math:

#     @classmethod
#     def add(cls,x,y):
#         if isinstance(x,(int,float)) and isinstance(y,(int,float)):
#             return x+y
#         else:
#             raise TypeError("Inuputs must be numbers")


#     # def add_instance(self,x,y):
#     #     if isinstance(x,(int,float)) and isinstance(y,(int,float)):
#     #         return x+y
#     #     else:
#     #         raise TypeError("Inuputs must be numbers")


# #print(math.add_instance(4,4))

# obj = math()
# print(obj.add(10,45))


# class myclass:
#     @staticmethod
#     def my_static():
#         print("THis is the static method")

# obj = myclass()
# obj.my_static()


# class car:
#     total_car = 0

#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#         car.total_car += 1

#     @classmethod
#     def get_total_car(cls):
#         return cls.total_car
    
#     # @classmethod
#     # def update_total_car(cls,new_total):
#     #     cls.total_car = new_total


#     def update_total_car(self,new_total):
#         car.total_car = new_total

# object = car("Huafisdf","asdfd")
# print(car.get_total_car())
# print(object.get_total_car())
# print(object.update_total_car(5))
# print(car.get_total_car())


# from abc import ABC,abstractmethod

# # Abstract Product
# class Animal(ABC):
#     #@abstractmethod
#     def speak(self):
#         pass

# # Concrete Products
# class Dog(Animal):

    
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"


# obj = Dog(Animal)
# print(Dog.speak())


# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using the function")
#     return mfx

# # @greet
# def add(x,y):
#     return x + y


# #@greet
# def hello():
#     print("Hello World")

# #hello()

# greet(add)(4,5)
# ans = add(5,19)
# print(ans)


# class mycalss:

#     def __init__(self,value):
#         self.value = value

#     def show(self):
#         print(f"Value is {self.value}")

#     @property
#     def ten_value(self):
#         return self.value * 10
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self.value = new_value /10

# obj = mycalss(10)
# # obj.ten_value = 67
# # print(obj.ten_value)
# # obj.show()
# obj.value = 67
# print(obj.value)
# obj.show()


# class HashTable:
#     def __init__(self):
#         self.Max = 100
#         self.arr = [None for i in range(self.Max)]

#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
        
#         return h % self.Max
    
#     def add(self,key,value):
#         h = self.get_hash(key)
#         self.arr[h] = value

#     def get(self,key):
#         h = self.get_hash(key)
#         return self.arr[h]

# obj = HashTable()
# obj.add("March 9",130)
# #print(obj.arr)
# ans = obj.get("March 9")
# print(ans)


# my_list = [1,2,3,4,5,6,7,8]
# print(my_list)
# my_list.insert(2,99)
# print(my_list)
# #del my_list[3]
# #my_list.remove(-1)
# my_list.pop(99)
# print(my_list)

# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_beg(self,data):
#         node = Node(data,self.head)
#         self.head = node

#     def print(self):
#         if self.head == None:
#             print("Linked List is empty !")
        
#         itr = self.head
#         lstr = ''

#         while itr:
#             lstr += str(itr.data) + '-->' + '\n'
#             itr = itr.next

#         print(lstr)

# l = LinkedList()
# l.insert_at_beg(5)
# l.insert_at_beg(89)
# l.print()


# text = 'geeKs For geEkS'
# print(text)
# # print(text.title())
# # print(text.replace("For","to"))
# print(text[6:8])

# my_string = "   Hello World   "
#print(my_string.strip())     # Output: "Hello World"
#print(my_string.replace("World", "Python"))  # Output: "   Hello Python   "
#print(" ".join(["Hello", "World"]))         # Output: "Hello-World"
#print(my_string.partition(" "))  # Output: ('', ' ', 'Hello World')
#print(my_string.split())        # Output: ['Hello', 'World']
# print("Hello\nWorld".splitlines())  # Output: ['Hello', 'World']


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beg(self,data):
#         new_data = Node(data)
#         new_data.next = self.head
#         self.head = new_data

#     def insert_at_end(self,data):
#         new_data = Node(data)
#         if not self.head:
#             self.head = new_data   
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node= last_node.next
#         last_node.next = new_data

#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")


#     # def display(self):
#     #     current_node = self.head
#     #     while current_node:
#     #         print(current_node.data, end=" -> ")
#     #         current_node = current_node.next
#     #     print("None")

# l = LinkedList()

# l.insert_at_beg(1)
# l.insert_at_beg(2)
# l.insert_at_beg(3)
# l.insert_at_end(4)
# l.display()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, data):
#         if not self.head:
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         current_node = self.head
#         while current_node.next:
#             if current_node.next.data == data:
#                 current_node.next = current_node.next.next
#                 return
#             current_node = current_node.next

#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#         current_node.next = new_node

#     def insert_at_beg(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def delete_node(self,data):
#         current_node = self.head
#         if current_node and current_node.data == data:
#             self.head = self.head.next
#             current_node = None
#             return
#         prev_node = None
#         while current_node and current_node.data != data:
#             prev_node = current_node
#             current_node = current_node.next
#         if current_node is None:
#             return
#         prev_node.next = current_node.next
#         current_node = None
    
#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data,end="->")
#             current_node = current_node.next
#         print("None")


# if __name__ == "__main__":
#     # Creating a linked list
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.insert_at_beg(0)

#     # Printing the linked list
#     linked_list.display()

#     # Deleting a node
#     linked_list.delete_node(2)
#     linked_list.display()


# filter_num = lambda characters: ('').join(chr for chr in characters if chr.isdigit())

# print(filter_num("Geeks101"))

# cube_func = lambda num: num ** 3

# print(cube_func(3))
# lst= ["RAM","SHYAM","KAAM"]

# print([val for val in map(lambda x : len(x),lst)])


# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def insert_at_beg(self,data)->None:
#         new_node = Node(data)
#         new_node.next  = self.head
#         self.head = new_node

#     def insert_at_end(self,data) -> None:
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         currnet_node = self.head
#         while currnet_node.next:
#             currnet_node = currnet_node.next
#         currnet_node.next = new_node

#     # def delete_node(self,data) -> None:
#     #     curent_node = self.head
#     #     while curent_node.next:
#     #         if curent_node.data == data:
#     #             curent_node = curent_node.next
#     #         curent_node = curent_node.next
#     def display(self)->None:
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next
#         print("None")

#     def display_at_middle(self)-> int:
#         my_dict = {}
#         my_list = []
#         index = 0
#         current_node = self.head
#         # while current_node:
#         #     my_dict[index] = current_node.data
#         #     current_node = current_node.next
#         while current_node:
#             my_list.append(current_node.data)
#             current_node = current_node.next

#         print(len(my_list))
#         mid = len(my_list) // 2
#         print(mid)
#         return my_list[mid]
#         # if len(my_dict) % 2 != 0:
#         #     #mid = mid + 1
#         #     return my_dict[mid]
#         # else:
#         #     return my_dict[mid - 1]

#     def reveres_linked_list(self):
#         current_node = self.head
#         prev_node = None
#         while current_node:
#             prev_node = current_node
#             current_node = current_node.next

#     def display_at_mid(self):
#         my_dict = {}
#         index = 0
#         current_node = self.head
#         while current_node:
#             my_dict[index] = current_node.data
#             current_node = current_node.next
#             index += 1

#         mid = len(my_dict) // 2
#         if len(my_dict)

# l = LinkedList()
# l.insert_at_end(11)
# l.insert_at_end(12)
# l.insert_at_end(13)
# l.insert_at_end(14)
# l.insert_at_end(15)
# #l.insert_at_end(16)
# # l.insert_at_beg(99)
# print(l.display_at_middle())
# #l.display()

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None


    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        
        return level

    def add_child(self,child):
        child.parent = self
        self.child.append(child)


    def display_tree(self):
        spaces = " " * self.get_level() * 3
        print(spaces,self.data)
        if self.child:
            for child in self.child:
                child.display_tree()

        

def build_product_tree():
    root = TreeNode("Electronics")

    Laptop = TreeNode("Laptop")
    Laptop.add_child(TreeNode("OMEN"))
    Laptop.add_child(TreeNode("ACER"))

    Mobile = TreeNode("Mobile")
    Mobile.add_child(TreeNode("Samsung"))
    Mobile.add_child(TreeNode("Oppo"))

    TV = TreeNode("Television")
    TV.add_child(TreeNode("32 Inch"))
    TV.add_child(TreeNode("55 Inch"))


    root.add_child(Laptop)
    root.add_child(Mobile)
    root.add_child(TV)



    root.display_tree()




if __name__ == '__main__':
    build_product_tree()

