def search_matrix(matrix, target):

    m = len(matrix)
    n = len(matrix[0])

    left = 0
    right = m*n - 1

    while left<= right:
        mid = (left+right)/2

        pivot_ele = matrix[mid//n][mid%n]

        if pivot_ele == target:
            return True

        elif pivot_ele > target:
            right = mid - 1

        else:
            left = mid + 1

    return False





print search_matrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 24)