
# def star(n):
#     for i in range(1,n+1):
#         print("* " * i)

# star(5)

# def my_func(n:int) -> None:
#     for i in range(n,0,-1):
#         print(i * "* ")

# my_func(5)

# n =5
# for i in range(n, 0, -1):
#     print(i)


# def right_triangel(n):
#     for i in range(n,0,-1):
#         print(n -1 * " " + (n-i) * "*")

# right_triangel(5)

# n=5


# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * i)

# def right_triangle(n):
#     for i in range(1,n+1):
#         print((n-i )* "" + i * "*")

# right_triangle(5)

# def pyramid(n):
#     for i in range(n):
#         #print((n-i//2) * " " + i * "*" + (n-i//2) * " ")
#         print(' ' * (n - i -1) + "*" * (2 * i +1))
# pyramid(5)

# Function to print a half pyramid pattern
# def half_pyramid(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print("* ", end="")
#         print("")

# # Example: Print a half pyramid with 5 rows
# n = 5
# half_pyramid(n)

# def my_pyramid(n):
#     for i in range(1,n+1):
#         print("* " * i)

# my_pyramid(5)

# def recursion_pyramid(n):
#     # if n > 0:
#     #     #print("*" * (n - (n-1)))
#     #     print(n * "*")
#     #     recursion_pyramid(n-1)
#     #     #print(n * "*")
#    for i in range(n,0,-1):
#       print(i)
# recursion_pyramid(5)

# def print_no_pyramid(n):
#     for i in range(1,n+1):
#         #print(f"{i }")
#         for j in range(i,n+1):
#             print(f"{j}",end="")
#         print('\n')

# print_no_pyramid(5)

# def py(n):
#     for i in range(1,n+1):
#         #print("*" * i)
#         for j in range(1,i+1):
#             #print(" " * j)
#             print(j,end="")
#         print("")

# py(5)

# def my_pyramid(n):
#     for i in range(1,n+1):
#         temp = i
#         print(f"{temp}" * i)
#         temp += 1
# my_pyramid(5)

# def your_pyramid(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print()

# your_pyramid(5)
# def half_rec_pyramid(n):
#     if n > 0:
#         half_rec_pyramid(n-1)
#         print(n * f"{n}")

# half_rec_pyramid(5)

# def no_pyramid(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()

# no_pyramid(5)

# def my_func(n):
#     num = 1
#     for i in range(1,n+1):
#         print(num)
#         num  += 1
# my_func(5)

# def aplha_pyramid(n):
#     char = 65
#     for i in range(1,n+1):
#         char = 65
#         for j in range(1,i+1):
#             #print(j,end="")
#             print(chr(char),end="")
#             char += 1
#         print()
# aplha_pyramid(5)

# def inverted_pyramid(n):
#     # for i in range(n):
#     #     for j in range(n-i):
#     #         print("*",end="")
            
#     #     print()

#     for i in range(n,0,-1):
#         for j in range(i):
#             print("* ",end="")
#         print()

# inverted_pyramid(5)


# # Function to print inverted half pyramid pattern
# def inverted_half_pyramid(n):
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print("* ", end="")
#         print("\r")

# # Example: Inverted Half Pyramid with n = 5
# n = 5
# inverted_half_pyramid(n)


# def print_hollow_inverted_half_pyramid(rows):
#     for i in range(rows, 0, -1):
#         for j in range(rows - i):
#             print(" ", end="")
#         for j in range(i):
#             if j == 0 or j == i - 1 or i == rows:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# # Example usage
# num_rows = 5
# print("Hollow Inverted Half Pyramid:")
# print_hollow_inverted_half_pyramid(num_rows)

# def full_pyramid(n):
#     for i in range(1,n+1):
#         #print(" " * (n//2 - i) + "*" * i)
#         #print(' ' * (n - i - 1) + '*' * i)
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# full_pyramid(5)
# def full_pyramid(rows):
#     for i in range(rows):
#         #print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
#         print(" " * (rows - i) + "*" * (2 * i + 1))
# full_pyramid(5)

# Function to print full pyramid pattern
# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()
   
# full_pyramid(5)

def full_pyramid(n):
    for i in range(1, n+1):
        for j in range(n - 1):
            print(" " ,end="")
        for k in range(1,2 * i):
            print("*",end="")
        print()

full_pyramid(5)

