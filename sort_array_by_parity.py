class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x%2 ==0]+ [x for x in A if x%2 ==1])

#Time complexity: O(N)
#Space complexity: O(N)
    
#In-Place sorting using quicksort  
   
    def sortArrayByParity1(self, A):
        i, j = 0, len(A)-1
        while i < j:
            if A[i] %2 > A[j] %2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A 

#Time complexity: O(N)
#Space complexity: O(1)




