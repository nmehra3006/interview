def binary_search(arr, key):

    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            left = mid + 1

        else:
            right = mid - 1

    return -1

print binary_search([0, 30, 40, 50, 60, 70, 80], 530)



