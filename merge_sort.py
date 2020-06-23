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

        mid = len(arr) // 2
        leftarr = arr[:mid]
        rightarr = arr[mid+1:]
        mergesort(leftarr)
        mergesort(rightarr)
        merge(leftarr, rightarr, arr)

    return arr


print mergesort([])
