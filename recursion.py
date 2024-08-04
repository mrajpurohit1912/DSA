# def print_no(n):
#     if (n > 0):
#         print_no(n - 1)
#         print(n)

# print_no(5)


# for i in range(5):
#     print(i)


# def print_n_to_1(n):
#     if n > 0:
#         print(n)
#         return print_n_to_1(n-1)


# def sum_of_n_rec(n):
#     sum_cal = 0
#     if n>0:
#         sum_cal += n
#         print(n)
#         return sum_of_n_rec(n-1)
#     else:
#         return sum_cal

# def sum_recursion(n):
#     if n <= 1:
#         return n
#     return n + sum_recursion(n-1) 

# ans = sum_recursion(5)
# print(ans)


# def rev_recursion(s):
    
#     if len(s) == 0:
#         return
    
#     temp = s[0]
#     rev_recursion(s[1:])
#     print(temp)


# s = "Hello"

# rev_recursion(s)
    

def string_len(arr):
    if arr == "":
        return 0
    else:
        return 1 + string_len(arr[1:])        
    
str = "GeeksforGeeks"

print(string_len(str))