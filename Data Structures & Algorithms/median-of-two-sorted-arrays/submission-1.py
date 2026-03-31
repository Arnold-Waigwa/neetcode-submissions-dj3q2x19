class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #get the left partition from both lists
        A = nums1
        B = nums2
        total = len(A) + len(B)
        Half = total // 2

        #make A the smaller one
        if len(A) > len(B):
            #swap
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = Half - i - 2

            #check if the partition is correct
            rightA = A[i + 1] if (i + 1) < len(A) else float("infinity")
            leftA = A[i] if i >= 0 else float("-infinity")
            rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")

            if leftA <= rightB and leftB <= rightA:
                #valid partition
                #need to find the median
                #if odd:
                if (total % 2) != 0:
                    #take the smaller of the right
                    median = min(rightA, rightB)
                    return median
                #max of left partition + min of right //2
                return (max(leftA, leftB) + min(rightA, rightB)) / 2

            elif leftA > rightB:
                    #need to reduce A partition
                r = i -1
            else:
                l = i + 1
