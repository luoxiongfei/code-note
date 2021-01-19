class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        for i in range(1,len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i-1][j]
        for i in range(len(matrix)):
            matrix[i].sort(reverse=True)
            for j in range(len(matrix[i])):
                if matrix[i][j] * (j + 1) > ans:
                    ans = matrix[i][j] * (j + 1)
        return ans
