from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.route = ["JFK"]

    # def findItiniery(self, tickets):
    #     d = defaultdict(list)
    #     for flight in tickets:
    #         d[flight[0]].append(flight[1])
    #     self.route = ["JFK"]
    #
    #     def dfs(start='JFK'):
    #         if len(self.route) == len(tickets) + 1:
    #             return self.route
    #
    #         myDsts = sorted(d[start])
    #
    #         for dst in myDsts:
    #             d[start].remove(dst)
    #             self.route.append(dst)
    #             worked = dfs(dst)
    #             if worked:
    #                 return worked
    #             self.route.pop()
    #             d[start] += dst,
    #
    #     return dfs()
    def find_itiniery(self, tickets):
        def dfs(d, root="JFK"):

            if self.route == len(tickets):
                print self.route
                return self.route

            destination = d[root]
            for dest in destination:
                d[root].remove(dest)
                self.route.append(dest)
                flag = dfs(d, dest)
                if flag:
                    return flag
                d[root].append(dest)
                self.route.pop()

        d = defaultdict(list)
        for ticket in tickets:
            src, dest = ticket[0], ticket[1]
            d[src].append(dest)

        for src in d:
            d[src].sort()

        dfs(d)
        return self.route


sol = Solution()
print sol.findItiniery([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])