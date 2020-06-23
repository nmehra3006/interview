def l_distance(str1, str2):
    def compute_distance(m, n):

        if m < 0:
            return n+1

        elif n < 0:
            return m+1

        if str1[m] == str2[n]:
            return compute_distance(m-1, n-1)

        sub_last = compute_distance(m-1, n-1)
        add_last = compute_distance(m, n-1)
        delete_last = compute_distance(m-1, n)

        return 1 + min(sub_last, add_last, delete_last)

    return compute_distance(len(str1) - 1, len(str2) - 1)

print l_distance("monday", "tuesday")
