class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        a = [[] for i in range(len(row)>>1)]
        ans = 0
        for i in range(len(row)>>1):
            if not a[row[i<<1]>>1]:
                a[row[i<<1]>>1].append(row[i<<1])
                a[row[i<<1]>>1].append(row[i<<1|1])
            else:
                while a[row[i<<1]>>1]:
                    a[row[i<<1]>>1][1],row[i<<1] = row[i<<1],a[row[i<<1]>>1][1]
                    ans += 1
                a[row[i<<1]>>1].append(row[i<<1])
                a[row[i<<1]>>1].append(row[i<<1|1])
        for i in range(len(a)):
            while a[i][1]>>1!=i:
                a[a[i][1]>>1][1],a[i][1]=a[i][1],a[a[i][1]>>1][1]
                ans += 1
        return ans
