def dutch_flag_problem(arr, pivot):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid < high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low +=1
            mid +=1
        elif arr[mid] == pivot:
            mid +=1
        else:
            high -=1
            arr[mid], arr[high] = arr[high], arr[mid]
    return arr


def dutch_flag_with_count(arr):

    c0 = 0
    c1 = 0
    c2 = 0

    i = 0
    while i < len(arr):

        if arr[i] == 0:
            c0 +=1

        elif arr[i] ==1:
            c1 +=1

        else:
            c2 +=1
    j = 0
    print arr
    while c0 > 0:
        arr[j] = 0
        j += 1
        c0 -= 1
    print arr

    while c1 > 0:
        arr[i] = 1
        i += 1
        c1 -= 1

    while c2 > 0:
        arr[i] = 2
        i += 1
        c2 -= 1
    print arr
    return arr

if __name__ == "__main__":
    print dutch_flag_problem([-3, 0, -1, 1, 1, 3, 4, 2], 1)
    #print dutch_flag_with_count([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])