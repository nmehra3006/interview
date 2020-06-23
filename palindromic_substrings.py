def palindromic_substrings(words):

    count = 0

    l = 1
    n = len(words)
    dp = [False for j in range(len(words)) for i in range(len(words))]
    while l <= n:
        i = 0
        # while i < n-l+1:
        #
        #     j = i + l - 1
        #
        #     if i == j:
        #         dp[i][j] = True
        #         count +=1
        #
        #     elif i + 1 == j:
        #         if words[i] == words[j]:
        #             dp[i][j] = True
        #             count += 1
        #     else:
        #         if words[i] == words[j] and dp[i + 1][j - 1]:
        #             dp[i][j] = True
        #             count += 1
        #     return count
        for l in range(1, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                if i == j:
                    dp[i][j] = True
                    res += 1
                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        res += 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
        return res

palindromic_substrings("aaa")
