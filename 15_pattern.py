def fillprefixsum(arr):
    prefix_arr = arr

    prefix_arr[0] = arr[0]

    for i in range(1,len(arr)):
        prefix_arr[i] = prefix_arr[i - 1] + arr[i]
    # for i in range(len(arr)):

    #     if i == 0:
    #         prefix_arr.append(arr[i])
    #     elif i == len(arr):
    #         prefix_arr.append(sum(arr))
    #     else:
    #         prefix_arr.append(sum(arr[:i+1]))

    return prefix_arr

def range_sum(prefix_sum, l, r):
    if l == 0:
        return prefix_sum[r]
    else:
        return prefix_sum[r] - prefix_sum[l - 1]


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    ans = fillprefixsum(arr)

    # arr = [10, 4, 16, 20]
    # n = len(arr)
 
    # # Function call
    # prefixSum = [0 for i in range(n + 1)]
    # print(arr)
    # print(prefixSum)
    print(ans)
    l, r = 1, 3
    print(range_sum(ans,l,r))

    l, r = 0, 4
    print(range_sum(ans,l,r))