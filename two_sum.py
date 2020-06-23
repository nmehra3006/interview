def two_sum(arr, target):


    idx_map = {v:i for i,v in enumerate(arr)}

    for idx in range(len(arr)):

        if target - arr[idx] in idx_map:
            if arr[idx] == target - arr[idx]:
                if len(arr[idx]) >= 2:
                    return idx, idx_map[target - arr[idx]]
                else:
                    return -1

            else:

                return idx, idx_map[target - arr[idx]]

        return -1