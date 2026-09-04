class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        n = total // 2

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = n - i - 2

            i_front = nums1[i + 1] if i + 1 < len(nums1) else float("inf")
            i_back = nums1[i] if i >= 0 else float("-inf")

            j_front = nums2[j + 1] if j + 1 < len(nums2) else float("inf")
            j_back = nums2[j] if j >= 0 else float("-inf")

            if i_front < j_back:
                l = i + 1

            elif j_front < i_back:
                r = i - 1

            else:
                if total % 2 != 0:
                    return min(i_front, j_front)

                return (max(i_back, j_back) + min(i_front, j_front)) / 2
