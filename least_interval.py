import heapq as hq
from collections import Counter
def least_interval(tasks, n):
    units = 0
    task_count = Counter(tasks)

    heap = []
    hq.heapify(heap)
    for k, v in task_count.iteritems():
        hq.heappush(heap, -v)



    while heap:
        temp_list = []
        for _ in range(n+1):
            units += 1
            if heap:
                job = hq.heappop(heap)
                if job != -1:
                    temp_list.append(job + 1)   
                    print "temp", temp_list
                if not heap and not temp_list:
                    break

        for job in temp_list:
            hq.heappush(heap, job)

    return units


print least_interval(["A","A","A","B","B","B"], 2)