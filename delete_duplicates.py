def duplicates(arr):

    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            arr[write_index] = arr[i]
            write_index +=1

    return arr[:write_index]

print duplicates([1, 3, 3, 3, 4, 5, 5, 5, 5, 6])