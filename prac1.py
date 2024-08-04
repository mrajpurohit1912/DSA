# import pandas as pd
# import numpy as np

# # Create DataFrame df
# data = {
#     'A': np.random.randint(1, 100, size=5),
#     'B': np.random.randint(1, 100, size=5),
#     'C': np.random.randint(1, 100, size=5)
# }
# df = pd.DataFrame(data)

# # Create DataFrame df2 with some missing values
# data_with_missing = {
#     'A': [np.random.randint(1, 100) if np.random.rand() > 0.2 else np.nan for _ in range(5)],
#     'B': [np.random.randint(1, 100) if np.random.rand() > 0.2 else np.nan for _ in range(5)],
#     'C': [np.random.randint(1, 100) if np.random.rand() > 0.2 else np.nan for _ in range(5)]
# }
# df2 = pd.DataFrame(data_with_missing)

# print("DataFrame df:")
# print(df)
# print("\nDataFrame df2 (with missing values):")
# print(df2)


# dict_1 = {'a':[1,2,3],
#  'b':[4,5,6],
#  'c':[7,8,9]}
# df1 = pd.DataFrame(dict_1)
# print(df1)


# dict_2 = {'a':[1,3],
#  'b':[5,6],
#  'c':[7,8,9]}
# df2 = pd.DataFrame(dict_2)
# print(df2)
# import pandas as pd
# import numpy as np

# # Create DataFrame df
# data = {
#     'A': np.random.randint(1, 100, size=5),
#     'B': np.random.randint(1, 100, size=5),
#     'C': np.random.randint(1, 100, size=5)
# }
# df = pd.DataFrame(data)

# # Create DataFrame df2 with some missing values
# data_with_missing = {}
# for col in df.columns:
#     data_with_missing[col] = [val if np.random.rand() > 0.2 else np.nan for val in df[col]]
# df2 = pd.DataFrame(data_with_missing)

# print("DataFrame df:")
# print(df)
# print("\nDataFrame df2 (with missing values):")
# print(df2)
# df2 = df2.fillna(df)
# print(df2)

# def func(n:int)->None:
#     if n>0:
#         print("before ",n)
#         func(n-1)
#         print("after ",n)
        

# func(5)
# from typing import List

# def mean_of_array(lst:List[int]) -> int:
#     sum_val = 0
#     for i in lst:
#         sum_val += i
#     print(sum_val)
#     return sum_val / len(lst)


# ans = mean_of_array([1,2,3,4,5])
# print(ans)


# from typing import List

# def recSum(n: int) -> int:
#     if n  < 2:
#         return n
#     return n + recSum(n-1)

# ans = recSum()
# print(ans)

# from typing import List

# def arrSum(lst: List[int],n:int) -> int:
#     if n <= 0:
#         return 0
#     else:
#         return arrSum(lst,n-1) + lst[n-1]


# arr = [1, 2, 3, 4, 5] 
# n = len(arr)
# ans = arrSum(arr,n)
# print(ans)

# lst = [1,2,3,4,5,6,7,8,9]



# result = 
# for i in range(1,5+1):
#     print(i)





# def factorial_loop(n):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# print(factorial_loop(5))  # Output: 120

# def fact1(n):
#     result = 1

#     for i in range(2,n+1):
#         result *= i
    
#     return result

# print(fact1(5))


# def fact2(n):
#     if n == 0:
#         return 1
#     else: 
#         return n * fact2(n-1)
    
# print(fact2(3))