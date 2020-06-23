

def merge(left, right, arr):
    i = j = k = 0
    L = left
    R = right
    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr

def mergesort(arr):

    if len(arr) > 1:

        mid = len(arr)//2
        left_array = arr[:mid]
        right_array = arr[mid:]

        mergesort(left_array)
        mergesort(right_array)
        merge(left_array, right_array, arr)

    return arr



print mergesort([2,1,3,4,7,6,5])