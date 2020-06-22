#implementing kadane algorithm for max contiguous sum subarray
def max_contiguous_subarray(arr):

    best_sum = 0
    current_sum = 0
    _start = 0
    start = 0
    end = -1
    for i in range(len(arr)):

        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0
            _start = i+1


        #current_sum = max(0, current_sum + arr[i])

        if best_sum < current_sum:
            best_sum = current_sum
            start = _start
            end = i

        #best_sum = max(best_sum, current_sum)

    return best_sum, start, end

print max_contiguous_subarray([-2, -3, 4, -1, -2, 1, 5, -3])