#[3,5,4,5,1] = > 2


def get_missing_entry(arr):


    for i in range(len(arr)):
        arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    for i in range(len(arr)):
        if arr[i] > 0:
            return i+1
    return None


print get_missing_entry([3,5,4,5,1])