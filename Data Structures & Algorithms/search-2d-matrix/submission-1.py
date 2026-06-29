class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for row in matrix:
        #     if target in row:
        #         return True
        # return False
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid=(l+r)//2
            row=mid//n
            col=mid%n
            val=matrix[row][col]
            if val==target:
                return True
            elif val<target:
                l=mid+1
            else:
                r=mid-1
        return False

        # m, n = len(matrix), len(matrix[0])
        # left, right = 0, m - 1

        # while left <= right:
        #     middle = (right + left) // 2
        #     if target >= matrix[middle][0] and target <= matrix[middle][-1]:
        #         #search col
        #         l,r = 0, n - 1
        #         while l <= r:
        #             m = (r + l) // 2
        #             if target == matrix[middle][m]:
        #                 return True
        #             if target < matrix[middle][m]:
        #                 r = m - 1
        #             else:
        #                 l = m + 1
        #         return False

        #     if target < matrix[middle][0]:
        #         right = middle - 1
                
        #     elif target > matrix[middle][-1]:
        #         left = middle + 1
        # return False