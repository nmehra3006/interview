def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:

        if low <= high and arr[high] > pivot:
            high -= 1

        elif low <= high and arr[low] < pivot:
            low += 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    return high


def quick_sort(array, start, end):
    # pick a random pivot index, get pivot value
    # partition arr around pivot val so that left array has all values less than pivot val and right array has all values greater than pivot

    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)


array = [29,99,27,41,66]
quick_sort(array, 0, 4)
print array