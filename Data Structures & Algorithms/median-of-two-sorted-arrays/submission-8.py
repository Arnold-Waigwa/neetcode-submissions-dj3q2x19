class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # you have two arrays; intuition is to get the mid of A, and get the remaining from B
        A, B = nums1, nums2
        if len(A) > len(B):  #for speed and for j to make sense
            B, A = A, B
        
        half = (len(A) + len(B)) // 2
        l, r = 0, len(A) - 1
        while True:
            i = (l+r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (1+i) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                #were valid, get the median
                #if odd take the max
                if (len(A) + len(B)) % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Bleft > Aright:
                l = i + 1
            else:
                r = i - 1
        