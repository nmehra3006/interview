def generate_permutations(arr):

    def helper(res, first):
        if first == len(arr) - 1:
            res.append(arr[:])

        for i in range(first, len(arr)):

            arr[first], arr[i] = arr[i], arr[first]

            helper(res, first+1)
            arr[first], arr[i] = arr[i], arr[first]

    res = []
    helper(res, 0)
    return res

print generate_permutations([1, 2, 3])