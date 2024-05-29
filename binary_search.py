def linear_search(lst,n):
    for index,i in enumerate(lst):
        if i == n:
            return index
    
    return 
        

def binary_search(lst,number):
    # mid = len(lst) // 2
    # start = 0
    # end = len(lst) -1
    # #mid = (start + end) // 2
    # print(mid)
    # if number == mid:
    #     return number
    # elif number < mid:
    #     end = mid-1
    # else:
    #     start = mid +1

    low = 0
    high = len(lst) - 1
    mid = 0

    while low<=high:
        mid = (low + high) // 2
        
        if lst[mid] == number:
            return mid
        elif lst[mid] > number:
            high = mid - 1
        else:
            low = mid +1

    return None






if __name__ == '__main__':
    lst = [12,15,17,19,21,24,45,67]
    number_to_find = 45

    lin_result = linear_search(lst,number_to_find)
    print(lin_result)


    bin_result = binary_search(lst,number_to_find)
    #binary_search(lst,number_to_find)
    print(bin_result)