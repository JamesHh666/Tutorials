class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, A_row in enumerate(A):
            A[i] = A[i][::-1]
            A[i] = [j^1 for j in A[i]]
        rtype = A
        return rtype
        
# Runtime: 40 ms, faster than 42.11% of Python online submissions for Flipping an Image.
