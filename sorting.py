# # # def bubble_sort(element):
# # #     for i in range(len(element) - 1):
# # #         for j in range(len(element) - i - 1):
# # #             #print(element[i],j+1," ")
# # #             if element[i] < element[j]:
# # #                 element[i], element[j] = element[j] , element[i] 

# # #     return element

# def bubble_sort(element):
#     for i in range(len(element) ):
#         for j in range(len(element) ):
#             if element[i] < element[j]:
#                 element[i], element[j] = element[j] , element[i] 

#     return element
# if __name__ == "__main__":
#     #lst = [7,8,9]
#     #lst = [9,8,7]
#     #lst = [9,8,7]
#     lst = [99,8,7,34,10,2,887]
#     ans = bubble_sort(lst)
#     print(ans)

# def bubble_sort(element):
#     n = len(element)

#     for i in range(n-1):
#         swapped = False
#         for j in range(n-i-1):
#             if element[j] > element[j+1]:
#                 element[j],element[j+1] =element[j+1] ,element[j] 
#                 swapped = True
#         if not swapped:
#             break
#     return element



# def bubble_sort(element,key):
#     n = len(element)

#     # for i in range(n-1):
#     #     swapped = False
#     #     for j in range(n-i-1):
#     #         if element[j] > element[j+1]:
#     #             element[j],element[j+1] =element[j+1] ,element[j] 
#     #             swapped = True
#     #     if not swapped:
#     #         break


#     for i in range(n-1):
#         swapped = False
#         for j in range(n - i - 1):
#             if element[j][key] > element[j+ 1][key ]:
#                 element[j],element[j+1] = element[j+1] , element[j]
#                 swapped = True
#         if not swapped:
#             break
#     return element



# if __name__ == "__main__":
#     #lst = [7,8,9]
#     #lst = [9,8,7]
#     #lst = [9,8,7]
#     #lst = [99,8,7,34,10,2,887]
#     elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
    
#     #ans = bubble_sort(lst)
#     ans = bubble_sort(elements,'name')
#     print(ans)



# def find_min_element(element):
#     min = 1000000000000000000
#     for i in range(len(element)):
#         if element[i] < min:
#             min = element[i]
#     return min



# if __name__ == "__main__":
#     element = [44,23,9,99,89,55]
    # ans = sorted(element)
    # print(ans)
    
    #print(find_min_element(element))


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n - i -1):
#             if arr[j] > arr[i]:
#                  arr[j] , arr[i] =  arr[i],arr[j] 

#     return arr

# arr = [5,1,6,3,4,9]

# print(bubble_sort(arr))

# def bubble_sort(element):
#     n = len(element)

#     for i in range(n-1):
#         swapped = False
#         for j in range(n-i-1):
#             if element[j] > element[j+1]:
#                 element[j],element[j+1] =element[j+1] ,element[j] 
#                 swapped = True
#         if not swapped:
#             break
#     return element

# def bubble_sort(element):
#     n = len(element)
#     for i in range(n):
#         for j in range(i,n):
#             if element[i] > element[j]:
#                 element[i], element[j] =  element[j],element[i]

#     return element

# arr = [99,5,1,6,3,4,9]
# ans = bubble_sort(arr)
# print(ans)

# def selection_sort(element):
#     for i in range(len(element)):
#         min_idx = i
#         for j in range(i+1,len(element)):
#             if element[j] < element[min_idx]:
#                 min_idx = j
#                 element[i] , element[min_idx] =  element[min_idx],element[i] 

#     return element


# arr = [99,5,1,6,3,4,9]
# ans = selection_sort(arr)
# print(ans)

# def bubble_sort(elements):
#     n = len(elements)
#     for i in range(n-1):
#         swapped = False
#         for j in range(n-i-1):
#             if elements[j] > elements[j+1]:
#                 elements[j] ,elements[j+1] = elements[j+1] ,elements[j]
#                 swapped = True
#         if not swapped:
#             break
#     return elements


# def bubble_sort(element):
#     n = len(element)

#     for i in range(n-1):
#         swapped = False
#         for j in range(n-i-1):
#             if element[j] > element[j+1]:
#                 element[j],element[j+1] =element[j+1] ,element[j] 
#                 swapped = True
#         if not swapped:
#             break
#     return element


# def selection_sort(elements):
#     n = len(elements)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1,n):
#             if elements[j] < elements[min_idx]:
#                 min_idx = j
#         elements[i],elements[min_idx] = elements[min_idx],elements[i]
#     return elements


# if __name__ == "__main__":
#     arr = [ 2, 1,  23,10]

#     ans = selection_sort(arr)
#     print(ans) 


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

numbers = [12, 11, 13, 5, 6]
print(insertion_sort(numbers))  # Output: [5, 6, 11, 12, 13]
