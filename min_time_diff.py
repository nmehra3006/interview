def find_min_time_diff(timePoints):
    Time = [int(t[:2]) * 60 + int(t[-2:]) for t in timePoints]
    sortedTime = sorted(Time)
    minimum = 1440
    for i in range(1, len(sortedTime)):
        diff = sortedTime[i] - sortedTime[i-1]
        minimum = min(minimum, diff)
    diff = sortedTime[0] - sortedTime[-1] + 1440

    return diff


find_min_time_diff(["23:59","00:00"])