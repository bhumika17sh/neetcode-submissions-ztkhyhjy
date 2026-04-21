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