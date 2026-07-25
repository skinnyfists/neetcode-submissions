class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.find_row(matrix, target)
        if row_index == None:
            return False
        row = matrix[row_index]
        left, right = 0, len(row) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if row[midpoint] == target:
                return True
            if target > row[midpoint]:
                left = midpoint + 1
            if target < row[midpoint]:
                right = midpoint - 1
        return False

    def find_row(self, matrix: List[List[int]], target: int) -> int:
        left, right = 0, len(matrix) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if matrix[midpoint][0] <= target <= matrix[midpoint][-1]:
                return midpoint
            if target > matrix[midpoint][-1]:
                left = midpoint + 1
            if target < matrix[midpoint][0]:
                right = midpoint - 1
        return None
