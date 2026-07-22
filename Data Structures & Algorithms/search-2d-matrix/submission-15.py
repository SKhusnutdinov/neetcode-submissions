class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            mid = l + ((r-l) // 2)
            col = mid % len(matrix[0])
            row = mid // len(matrix[0])
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False