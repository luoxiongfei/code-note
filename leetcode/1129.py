class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        al = [float('inf') for i in range(n)]
        ar = [float('inf') for i in range(n)]
        edg = [[] for i in range(n)]
        for i in red_edges:
            edg[i[0]].append([i[1],0])
        for i in blue_edges:
            edg[i[0]].append([i[1],1])
        stk = [[0,0],[0,1]]
        al[0],ar[0] = 0,0
        while(stk):
            tmp = stk.pop(0)
            for i in edg[tmp[0]]:
                if tmp[1]^i[1]:
                    if i[1] and ar[tmp[0]] + 1 < al[i[0]]:
                        al[i[0]] = ar[tmp[0]] + 1
                        stk.append([i[0],i[1]])
                    elif not(i[1]) and al[tmp[0]] + 1 < ar[i[0]]:
                        ar[i[0]] = al[tmp[0]] + 1
                        stk.append([i[0],i[1]])
        ans = [min(al[i],ar[i]) for i in range(len(al))]
        for i in range(len(ans)):
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans
