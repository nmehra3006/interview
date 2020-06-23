def generate_permutation(string):
    res = []

    def helper(nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            helper(nums[:i] + nums[i + 1:], path + nums[i], res)

    helper(string, "", res)
    return res


print generate_permutation("abc")