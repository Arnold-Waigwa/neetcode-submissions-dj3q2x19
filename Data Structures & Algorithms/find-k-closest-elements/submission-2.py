class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)

        # Find insertion point for x
        while l < r:
            mid = (l + r) // 2

            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid

        # l is the first element >= x
        right = l
        left = l - 1

        res = []

        for _ in range(k):
            left_dist = abs(arr[left] - x) if left >= 0 else float("inf")
            right_dist = abs(arr[right] - x) if right < len(arr) else float("inf")

            if left_dist <= right_dist:
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

        return sorted(res)