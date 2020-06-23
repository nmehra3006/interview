def trap_water(arr):
    amount = 0

    i = 0
    j = len(arr) - 1
    max_left = 0
    max_right = 0
    res = 0

    while i <= j:
        max_left = max(max_left, arr[i])
        max_right = max(max_right, arr[j])

        if max_left <= max_right:

            res += max_left - arr[i]
            i +=1

        else:
            res += max_right - arr[j]
            j -=1

    return res


print trap_water([0,1,0,2,1,0,1,3,2,1,2,1])


