def pivot_array(arr, idx):

    left = 0
    mid = 0
    pivot = arr[idx]
    right = len(arr)


    while mid < right:
        if arr[mid] < pivot:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            right -= 1
            arr[mid], arr[right] = arr[right], arr[mid]

    return arr


print pivot_array([4, 6,1,11,-2,6,-9,10,21,14,2,-4,4,0,7], 7)