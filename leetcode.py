# git checkout origin/main -- leetcode.py
# two sum
# from typing import List

# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         tg = target
# #         for i in range(len(nums)):
# #             if nums[i] + nums[i+1] == target:
# #                 return [i,i+1]


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

# # nums = [2,7,11,15]
# # target = 9
# # nums = [3,2,4]
# # target = 6

# nums = [3,3] 
# target = 6



# # ans = Solution()
# # print(ans.twoSum(nums=nums,target=target))

###########################################################################
# # 13. Roman to Integer

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_numerals_dict = {
#                                 'I': 1,
#                                 'V': 5,
#                                 'X': 10,    
#                                 'L': 50,
#                                 'C': 100,
#                                 'D': 500,
#                                 'M': 1000
#                                }
#         # count = 0
#         # for i in s:
#         #     if i == roman_numerals_dict[i]:
#         #         count += 
#         # return count
#         # count = 0
#         # for key,value in roman_numerals_dict.items():
#         #     for i in s:
#         #         if i == key:
#         #             count += value

#         # return count

#         result = 0
#         prev_val = 0

#         for i in s:
#             value = roman_numerals_dict[i]
#             if value >  prev_val:
#                 result += value - 2 * prev_val
#             else:
#                 result += value
#             prev_val = value
#         return result

# #s = "III"
# s = "MCMXCIV"
# sl = Solution()
# print(sl.romanToInt(s))
###########################################################################
# 14. Longest Common Prefix
# from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # result = ""
        # for index,i in enumerate(strs):
        #     if index == 0:
        #         pass
        #     elif i[index] == i[index - 1]:
        #         result += i[index]
        # return result

        # result = ""
        # # for i in strs:
        # #     print(*i)
        # for i in zip(*strs):
        #     print()

#         if not strs:
#             return ""

#         result = ""

#         for index, char in enumerate(str[0]):
#             for string in strs[1:]:
#                 if index >= len(string) or string[index] != char:
#                     return result
#             result += char
#         return result

# strs = ["flower","flow","flight"]

# sl = Solution()
# print(sl.longestCommonPrefix(strs))

# for i in strs[1:]:
#     print(i)

###########################################################################

# 20. Valid Parentheses

# class Solution:
#     def isValid(self, s: str) -> bool:        
#         # counter = ""
#         # for i in s:
#         #     if i not in counter:
#         #         counter += i
#         #     else:
#         #         return 

#         my_dict = {'(':')',
#                    '[':']',
#                    '{':'}'
#                    }
#         for key,value in my_dict:
#             for i in s:
#                 for j in s[1:]:
#                     if i == key & j != value:
#                         return False
                    
#                     else:
#                         return True


# s = "()"
# sl = Solution()
# print(sl.isValid(s))
###############################################################################
# 35. Search Insert Position        
# from typing import List

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         # for i in range(len(nums)):
#         #     if target == nums[i]:
#         #         return i
#         #     elif nums[i] > target:
#         #         return i
#         #     elif i == len(nums):
#         #         return i


#         l,r = 0,len(nums) - 1

#         while l <= r:
#             mid = l + (r - l) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 return mid + 1
#             else:
#                 right = mid - 1

#         return l            
        


# nums = [1,3,5,6]
# sl = Solution()
# ans = sl.searchInsert(nums,7)

# print(ans)

########################################################################################
# 20. Valid Parentheses

# class Solution:
#     def isValid(self, s: str) -> bool:
#         my_dict = {'(':')',
#                    '{':'}',
#                    '[':']'}
        
#         stack = []
#         # for i in range(len(s)):
#         #     for key,value in my_dict.items():                    
#         #         if s[i] == key:
#         #             val_key = key
#         #         if 
                    
#         # for char in s:
#         #     if char in my_dict:
#         #         top_element = stack.pop() if stack else '#'
#         #         if my_dict[char] != top_element:
#         #             return False
                
#         #     else:
#         #         stack.append(char)

#         # return not stack

#         # for c in s:
#         #     if c == '(':
#         #         stack.append(')')
#         #     elif c == '{':
#         #         stack.append('}')
#         #     elif c == '[':
#         #         stack.append(']')
#         #     elif not stack or  stack.pop() != c:
#         #         return False

#         # return not stack      

#         for i in s:
#             if i in my_dict:
#                 if not stack or stack.pop() != my_dict[i]:
#                     return False
#             else:
#                 stack.append(i)

#         return not stack

# s = "()[]{}"  
# sl = Solution()

# ans  = sl.isValid(s)
# print(ans)
# my_dict = {'(':')',
#                    '{':'}',
#                    '[':']'}

# for i in range(len(my_dict)):
#     print(my_dict[i])
########################################################################################
#7. Reverse Integer
# class Solution:
#     def reverse(self, x: int) -> int:
#         INT_MIN = -2** 31
#         INT_MAX = 2** 31 - 1
#         rev_x = 0
#         sign = 1 if x >= 0 else -1
#         x = abs(x)

#         while x!=0:
#             last_digit = x % 10
#             rev_x  = rev_x * 10 + last_digit
#             x //= 10

#         rev_x = rev_x * sign
#         if rev_x < INT_MIN or rev_x > INT_MAX:
#             return 0
#         else:
#             return rev_x
# sl = Solution()
# print(sl.reverse(123))
# print(sl.reverse(-123))
# print(sl.reverse(120))

# x = 564

# reversed_x = 0
# while x != 0:
#     last_digit = x % 10
#     reversed_x = reversed_x * 10 + last_digit
#     x //= 10

# print(reversed_x)
#############################################################################
# 39. Combination Sum
# from typing import List

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         if len(candidates) == 0 or target < candidates[0]:
#             return None
#         else:
#             final_tgt = []
#             tgt = []
#             for i in candidates:
#                 if i == target:
#                     final_tgt.append([i])
#                 tgt.append(i)
#                 if sum(tgt) == target:
#                     final_tgt.append(tgt)
                    



# candidates = [2,3,6,7]
# target = 7
# sl = Solution()
# sl.combinationSum(candidates,target)
##############################################################################
# 88. Merge Sorted Array
# from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1.extend(nums2)
#         #nums1 = list(filter(lambda x : x != 0,nums1))
#         #nums1 = [ i for i in nums1 if i != 0]
#         print(nums1)
#         # for i in nums1:
#         #     if i == 0:
#         #         nums1.remove(i)
#         while 0 in nums1:
#             nums1.remove(0)
#         print(nums1)
#         print(sorted(nums1))
#         print(nums1)
##############################################################################
        
# 67. Add Binary

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         result = ''
#         carry = 0

#         i,j = len(a) - 1,len(b) - 1

#         while i >= 0 or j >= 0:
#             digit_a = int(a[i]) if i > 0 else 0
#             dight_b = int(b[j]) if j > 0 else 0

#             curr_sum = digit_a + dight_b + carry
#             result = str(curr_sum % 2) + result
#             carry = curr_sum // 2

#             i -= 1
#             j -= 1

#         if carry:
#             result = "1" + result
# sl = Solution()
# sl.addBinary()
######################################################################################
# 2. Add Two Numbers

# class ListNode:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             sum_val = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carry
#             carry = sum_val // 10
#             digit = sum % 10

#             current.next=ListNode(digit)
#             current = current.next

#             if l1:
#                 l1.next
#             if l2:
#                 l2.next
        
#         return dummy.next
# l1 = ListNode(2)
# l1.next = ListNode(6)
# l1.next.next = ListNode(4)


# l2 = ListNode(6)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# # Create solution object
# solution = Solution()

# # Call the function
# result = solution.addTwoNumbers(l1, l2)

# # Print the result
# while result:
#     print(result.val, end=" ")
#     result = result.next

######################################################################################
# 39. Combination Sum
# from typing import List

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         main_lst = []
#         sum_lst = []
#         for i in candidates:
#             sum_lst.append(i)
#             if sum(sum_lst) == target:
#                 main_lst.append(sum_lst)
#                 sum_lst = []
#         return main_lst

# if __name__ == '__main__':
#     candidates = [2,3,6,7]
#     target = 7
#     sl = Solution()
#     ans = sl.combinationSum(candidates,target)
#     print(ans)

######################################################################################
# 24. Swap Nodes in Pairs
# from typing import Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Create a dummy node which acts as the pre-head of the list
#         dummy = ListNode(0)
#         dummy.next = head
#         prev_node = dummy

#         # Traverse the list in pairs
#         while head and head.next:
#                 # Identify the nodes to be swapped
#                 first_node = head
#                 second_node = head.next

#                 # Swapping the nodes
#                 prev_node.next = second_node
#                 first_node.next = second_node.next
#                 second_node.next = first_node

#                 # Move the pointers forward for the next pair
#                 prev_node = first_node
#                 head = first_node.next

#         # The new head of the list is the next node of dummy
#         return dummy.next
                        
                

# def create_linked_list(vals):
#     if not vals:
#         return None
#     head = ListNode(vals[0])
#     current = head
#     for val in vals[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head

# sl = Solution()
# head = [1,2,3,4]
# print(sl.swapPairs(head))

#############################################################################################

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         lst = []
#         lst1 = []

#         while len(s) != 0:
#             for i in s:
#                 if i in lst:
#                     lst1.append(lst)
#                     lst = []
#                     idx = s.index(i)
#                     s = s[idx:]
#                     #break
#                 elif not i in lst:
#                     lst.append(i)


#         #return len(max(lst1))
#         return lst1
    

# s = "pwwkew"
# sl = Solution()
# print(sl.lengthOfLongestSubstring(s))


# lst = [[1,2,3],[1,2,3,4]]

# print(len(max(lst)))


# def my_func(s: str) -> int:
#     lst = []
#     lst1 = []
#     for i in s:
#         if i in lst:
#             lst1.append(lst)
#             lst = []
#             s = s[i:]
#             break
#         elif not i in lst:
#             lst.append(i)


#     return len(max(lst1))

# s = "ABCDE"
# start = 0
# end = len(s)

# while start<=end:
#     print(s[start],start)
#     start +=1

# Definition for singly-linked list.
# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         current_node = head
#         while(current_node):
#             print(current_node)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class my_class:
#     def Display(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         length = 0
#         current = head
#         while current:
#             current = current.next
#             length += 1

#         if length == n:
#             if head.next:
#                 return head.next
#             else:
#                 return None
        
#         idx = 1

#         current_node = head
#         while(idx < length - n):
#             current_node = current_node.next
#             idx += 1

#         current_node.next = current_node.next.next

#         return head
            

# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)

#     cl = my_class()
#     print(cl.Display(head=head,n=2))

from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums) - 1):
#             if nums[i] +nums[i + 1] == target:
#                 lst = [i,i+1]
#                 return lst

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for 
#             for j in range(i+1)

# nums = [2,7,11,15]
# target = 9
# sl = Solution()
# print(sl.twoSum(nums,target))

# lst = [88,43,455,65,676]

# for i in range(len(lst) - 1):
#     print(lst[i])


lst1 = [101,102,103,104]
#lst2 = [201,202,203,204]

for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        print(lst1[i],lst1[j])