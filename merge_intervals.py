def merge_intervals(intervals):

    intervals.sort()

    res = []
    res.append(intervals[0])
    for interval in intervals[1:]:
        # non - overlapping
        start, end = res[-1][0], res[-1][1]
        if interval[0] > end:
            res.append(interval)

        elif interval[0] < end and interval[1] <= end:
            continue

        elif interval[0] < end and interval[1] > end:
            res.pop()
            res.append([min(start, interval[0]), max(interval[1], end)])

    return res

print merge_intervals([[1,3],[2,6],[8,10],[15,18]])
