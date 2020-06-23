def check_duplicates(arr):

    sum_arr = sum(arr)
    print sum_arr
    n = len(arr)
    sum_n = n*(n-1)/2
    print sum_n
    return   (sum(arr) - sum(set(arr)))//len(arr) - len(set(arr))


print check_duplicates([1,2,3,4,5,6,6,7])