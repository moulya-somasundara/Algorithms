class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        j= 0
        ans = []
        while j< N and A[j]<0:
            j += 1
            i = j-1
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else: 
                ans.append(A[j]**2)
                j += 1
        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1
        return ans
    
s = Solution()
A = [-3, -2, -1, 4, 5, 6]
print(s.sortedSquares(A))

