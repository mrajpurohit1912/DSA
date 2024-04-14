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
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         return i
        #     elif nums[i] > target:
        #         return i
        #     elif i == len(nums):
        #         return i


        l,r = 0,len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return mid + 1
            else:
                right = mid - 1

        return l            
        


nums = [1,3,5,6]
sl = Solution()
ans = sl.searchInsert(nums,7)

print(ans)