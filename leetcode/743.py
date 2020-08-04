class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        stk = [K]
        ans = 0
        a = [float('inf') for i in range(N + 1)]
        a[K] = 0
        edg = [[] for i in range(N + 1)]
        for i in times:
            edg[i[0]].append([i[1],i[2]])
        while stk:
            tmp = []
            for i in stk:
                for j in edg[i]:
                    if a[j[0]] > a[i] + j[1]:
                        a[j[0]] = a[i] + j[1]
                        tmp.append(j[0])
            stk = tmp
        ans = max(a[1:])
        if ans == float('inf'):
            return -1
        return ans
